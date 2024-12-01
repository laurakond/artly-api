from rest_framework import generics, permissions
from .models import Artwork
from .serializers import ArtworkSerializer
from artly_api.permissions import IsOwnerOrReadOnly


class ArtworkList(generics.ListCreateAPIView):
    serializer_class = ArtworkSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Artwork.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
