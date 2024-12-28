from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model allows the users to follow and be followed back by other
    users by clicking an icon. Related to the owner and followed.
    :model:'auth.User'
    'unique_together' makes sure a user can't follow the same user twice.
    This part of code(followers functionality) has been taken from the Code
    Institute's DRF Api walkthrough (details in the README.md).
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
