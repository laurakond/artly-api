from django.db.models import Count
from rest_framework import generics
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Class to display all created profiles."""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_at')


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """ Retrieves the user's profile and allows to update it."""
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all().order_by('-created_at')