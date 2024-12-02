from rest_framework import generics, permissions
from .models import Artwork
from .serializers import ArtworkSerializer
from artly_api.permissions import IsOwnerOrReadOnly


class ArtworkList(generics.ListCreateAPIView):
    """Function to display all artwork posts in a list."""
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Artwork.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Function to display, edit and delete artwork post instance that belongs
    to logged in user only.
    """
    serializer_class = ArtworkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Artwork.objects.all()