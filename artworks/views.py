from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Artwork
from .serializers import ArtworkSerializer


class ArtworkList(generics.ListCreateAPIView):
    """Function to display all artwork posts in a list."""
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Artwork.objects.annotate(
        bids_count=Count('bids', distinct=True)).order_by('-updated_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'style',
        'type',
        'created_at'
    ]
    search_fields = [
        'artwork_title',
        'artist_name',
        'location',
        'payment_method',
        'style',
        'type'
    ]
    filterset_fields = [
        'style',
        'type',
        'price',
        'owner',
        'sold',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Function to display, edit and delete artwork post instance that belongs
    to logged in user only.
    """
    serializer_class = ArtworkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Artwork.objects.annotate(
        bids_count=Count('bids', distinct=True)).order_by('-updated_at')