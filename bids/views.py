from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, PermissionDenied
from artly_api.permissions import IsOwnerOrReadOnly, IsSellerOrReadOnly
from .models import Bid, Artwork
from .serializers import BidSerializer, BidDetailSerializer


class BidList(generics.ListCreateAPIView):
    """Function to display all bids related to one artwork in a list."""
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
        # get the validated artwork from the serializer as the serializer
        # is where that data is coming from
        artwork = serializer.validated_data['artwork']
        bid_price = serializer.validated_data['bid_price']

        if artwork.owner == self.request.user:
            raise ValidationError("You cannot bid on your own artwork.")

        instance = serializer.save(buyer=self.request.user)

        # Evaluate if the bid offer is lower that the asking price and send
        # appropriate response/update status
        # if bid_price < artwork.price:
        #     instance.status = "Rejected"
        #     instance.save()

        # if bid_price <= 0:
        #     raise ValidationError("you can only input values above 0.")

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     if response.data.get('status') == "Rejected":
    #         return Response(
    #             {"bid_price": "The bid is lower than the asking price."},
    #             status=status.HTTP_202_ACCEPTED
    #         )

    #     return response


class BidDetail(generics.RetrieveUpdateAPIView):
    """
    Function to display, edit and delete a bid that belongs
    to logged in user only. The bid field can be submitted only by the buyer
    and not the seller of the artwork.
    """
    serializer_class = BidDetailSerializer
    permission_classes = [
        IsSellerOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Bid.objects.all()

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        # Logic to prevent the buyer from editing their bid.
        if user != obj.seller:
            raise PermissionDenied(
                {"message": "You don't have access to modify this bid."}
            )
        return obj

    def put(self, request, *args, **kwargs):
        """
        Takes each bid instance, evaluates, updates the bid status and the
        artwork's sold field. Depending on the status, it will send appropriate
        message to the user and disable the bid functionality if the artwork
        object is sold.
        This part of the code was written with the help of DRF REST
        documentation and parts of it were appropriated from a fellow student's
        work. See the README.md for full credit/information.
        """

        instance = self.get_object()
        initial_status = instance.status

        # Check if the initial artwork status is sold in both Bid and Artwork
        # models, and if so, throw a message stating that.
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

        # Updates Artwork sold field to true if the bid status is sold.
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
