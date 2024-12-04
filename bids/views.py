from django.core.exceptions import ValidationError
from rest_framework import generics, permissions
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Bid
from .serializers import BidSerializer


class BidList(generics.ListCreateAPIView):
    """Function to display all bids related to one artwork in a list."""
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bid.objects.all()


    def perform_create(self, serializer):
        # get the validated artwork from the serializer as the serializer
        # is where that data is coming from 
        artwork = serializer.validated_data['artwork']
        if artwork.owner == self.request.user:
            raise ValidationError("You cannot bid on your own artwork.")
        serializer.save(buyer=self.request.user)


class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Function to display, edit and delete a bid that belongs
    to logged in user only.
    """
    serializer_class = BidSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bid.objects.all()