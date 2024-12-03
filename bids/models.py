from django.db import models
from django.contrib.auth.models import User
from artworks import Artwork


STATUS = [
    ('Pending', 'Pending'),
    ('Approve', 'Approve'),
    ('Reject', 'Reject'),
    ('Sold', 'Sold'),
]


class Bid(models.Model):
    """
    Stores information related to a bid which is attached to an
    individual artwork post.
    :model:'auth.User', :model:'Artwork'
    """

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyer'
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seller'
    )
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        related_name='artwork'
    )
    bid_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False
    )
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f'{self.buyer} bid {self.bid_price} for {self.artwork}'
