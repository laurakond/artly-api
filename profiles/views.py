from django.db.models import Count, Q
from rest_framework import generics, filters
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Displays all created profiles and generates a filter field."""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        artwork_count=Count('owner__artwork', distinct=True),
        sold_artwork_count=Count(
            'owner__artwork',
            distinct=True,
            filter=Q(owner__artwork__sold=True)
        ),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'artwork_count',
        'sold_artwork_count'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieves the user's profile and allows to update it.Calculates sold
    artwork count to display the users based on the count.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        artwork_count=Count('owner__artwork', distinct=True),
        sold_artwork_count=Count(
            'owner__artwork',
            distinct=True,
            filter=Q(owner__artwork__sold=True)
        ),
    ).order_by('-created_at')