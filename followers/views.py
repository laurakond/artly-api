from rest_framework import generics, permissions
from artly_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    View a list of all followers, i.e. all instances of a user
    following another user.
    Allows to follow another user only if the user is logged in.
    Perform_create method associates the current logged in user with
    a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower by id.
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
