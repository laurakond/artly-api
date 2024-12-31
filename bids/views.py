from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import Bid, Artwork
from .serializers import BidSerializer, BidDetailSerializer


class BidList(generics.ListCreateAPIView):
    """
    Function to display all bids related to one artwork in a list. Generates
    filter and search fields for the bids. Evaluates who the bidder is and
    prevents the seller to bid on their own artworks.
    """
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bid.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    ordering_fields = [
        'artwork__artwork_title',
        'artwork_id',
        'created_at',
        'status',
        'updated_at'
    ]
    search_fields = [
        'status',
        'artwork__artwork_title'
    ]
    filterset_fields = [
        'bid_price',
        'artwork'
    ]

    def perform_create(self, serializer):
        """
        Applies two validations to prevent the seller to bid on their own
        artwork, and for the buyer to submit a bid for the artwork that is
        already sold.
        """
        # get the validated artwork from the serializer as the serializer
        # is where that data is coming from
        artwork = serializer.validated_data['artwork']
        bid_price = serializer.validated_data['bid_price']

        if artwork.owner == self.request.user:
            raise ValidationError("You cannot bid on your own artwork.")

        if artwork.sold:
            raise ValidationError(
                "This artwork is no longer available for purchase."
            )

        instance = serializer.save(buyer=self.request.user)


class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Displays the buyer's bid, and edits(seller only) a bid that belongs to the
    seller. Evaluates who the logged in user is and prevents the buyer from
    editing the bid.
    """
    serializer_class = BidDetailSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Bid.objects.all()

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        # Logic to prevent the wrong user(not logged in) to edit a bid.
        if user != obj.seller and user != obj.buyer:
            raise PermissionDenied(
                {"message": "You don't have access to modify this bid."}
            )
        return obj

    def put(self, request, *args, **kwargs):
        """
        Put method for the seller of the artwork. Takes each bid instance,
        evaluates, and updates the bid status and the Artwork model's sold
        field.
        Depending on the status, it will send appropriate message to the user
        and disable the bid functionality if the artwork object is sold.
        The put method was written with the help of DRF REST documentation and
        parts of it were appropriated from a fellow student's project.
        See the README.md for full credit/information.
        """

        instance = self.get_object()
        initial_status = instance.status
        user = self.request.user

        # Checks that the user who can edit the bids status is the seller of
        # the artwork
        if user != instance.seller:
            raise PermissionDenied({
                "message": "Only the seller can modify this bid."
            })

        # Checks if the initial artwork status is 'sold' in both Bid and
        # Artwork models, and if so, throw a message stating that.
        if initial_status == "Sold" or instance.artwork.sold:
            return Response(
                {"message": "Artwork is no longer available for purchase."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Deserialize the status and check if the new returned status is valid.
        # If it is not, raise an exception. Includes partial validation.
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)

        # extract artwork status
        updated_status = serializer.validated_data.get('status')

        # Updates Artwork sold field to true if the bid status is 'sold'.
        if updated_status == "Sold":
            instance.artwork.sold = True
            instance.artwork.save()
            self.perform_update(serializer)

            return Response({
                "message":
                "Bid accepted and the artwork is no longer available.",
            }, status=status.HTTP_200_OK)

        # Does not allow to change the bid status because the sold field in the
        # Artwork model is already set to True(sold).
        elif initial_status == "Sold" and updated_status != "Sold":
            raise MethodNotAllowed(method=request.method)

        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Validates the user and allows only the owner of the bid to
        delete it.
        """
        instance = self.get_object()
        user = self.request.user

        # Checks that the user is the buyer and throws an error message if not
        if user != instance.buyer:
            raise PermissionDenied(
                {"message": "Only the buyer can delete this bid."}
            )

        self.perform_destroy(instance)
        return Response(
            {"message": "Bid deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
