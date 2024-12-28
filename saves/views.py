from rest_framework import generics, permissions
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Save
from .serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    """
    View all saved artworks in a list. Allows to save an artwork only if the
    user is authenticated.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a saved artwork by id.
    Delete(i.e. destroy) the save and remove from the saved artworks list.
    Only allows to do so if the user is the owner of the save.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
