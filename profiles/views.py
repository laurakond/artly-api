from django.db.models import Count
from rest_framework import generics, filters
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Class to display all created profiles."""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        artwork_count=Count('owner__artwork', distinct=True),
        sold_artwork_count=Count('owner__artwork__sold', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'artwork_count',
        'sold_artwork_count'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """ Retrieves the user's profile and allows to update it."""
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        artwork_count=Count('owner__artwork', distinct=True),
    ).order_by('-created_at')