from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Artwork
from .serializers import ArtworkSerializer


class ArtworkList(generics.ListCreateAPIView):
    """
    Displays all artworks in a list. Allows to filter and search the list based
    on the needed criteria.
    """
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
        'bids_count',
        'created_at'
    ]
    search_fields = [
        'artwork_title',
        'artist_name',
        'location',
        'payment_method',
        'style',
        'type',
        'owner__username'
    ]
    filterset_fields = [
        'style',
        'type',
        'price',
        'owner',
        'sold',
        'owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Displays, edits and deletes the artwork that belongs to logged in user
    only. Displays the number of bids the artwork has.
    """
    serializer_class = ArtworkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Artwork.objects.annotate(
        bids_count=Count('bids', distinct=True)).order_by('-updated_at')
