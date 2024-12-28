from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork


class Save(models.Model):
    """
    Save model enables the user to save an artwork by clicking on the save
    icon. 'unique_together' field prevents the user to save the same artwork
    more than once.
    :model:'auth.User'
    :model:'Artwork'
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(
        Artwork, related_name='saves', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'artwork']

    def __str__(self):
        return f'{self.owner} {self.post}'
