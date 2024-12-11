from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework import generics, permissions
from artly_api.permissions import IsOwnerOrReadOnly, IsSellerOrReadOnly
from .models import Bid, Artwork
from .serializers import BidSerializer, BidDetailSerializer


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


class BidDetail(generics.RetrieveUpdateAPIView):
    """
    Function to display, edit and delete a bid that belongs
    to logged in user only.
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
            raise ValidationError("You don't have access to modify this bid.")
        return obj


    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        # serializer_class = BidDetailSerializer
