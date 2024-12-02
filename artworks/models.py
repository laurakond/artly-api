from django.db import models
from django.contrib.auth.models import User

STYLE = [
    ('Modern', 'Modern'),
    ('Contemporary', 'Contemporary'),
    ('Digital art', 'Digital art'),
    ('Old Masters', 'Old Masters'),
    ('Classical', 'Classical'),
    ('Other', 'Other')
]

TYPE = [
    ('Collage', 'Collage'),
    ('Drawing', 'Drawing'),
    ('Needlework', 'Needlework'),
    ('Etching', 'Etching'),
    ('Painting', 'Painting'),
    ('Photography', 'Photography'),
    ('Pottery', 'Pottery'),
    ('Scultpure', 'Scultpure'),
    ('Watercolour', 'Watercolour'),
    ('Other', 'Other')
]

PAYMENT = [
    ('Paypal', 'Paypal'),
    ('Cash', 'Cash')
]


class Artwork(models.Model):
    """
    Stores information related to an individual Artwork post. 
    :model:'auth.User'
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork_title = models.CharField(max_length=150, blank=False)
    artist_name = models.CharField(
        max_length=250,
        blank=True,
        default='Unknown'
    )
    description = models.TextField(blank=False)
    style = models.CharField(
        max_length=150,
        choices=STYLE,
        default='Other'
    )
    type = models.CharField(
        max_length=100,
        choices=TYPE,
        default='Other'
    )
    payment_method = models.CharField(
        max_length=100,
        choices=PAYMENT,
        default='Cash'
    )
    price = models.DecimalField(
        blank=False,
        default=0.00,
        decimal_places=2,
        max_digits=10
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_urnaqw',
        blank=True
    )
    alt_text = models.CharField(
        max_length=100,
        unique=False,
        blank=True,
        default='Artwork image'
    )
    contact = models.CharField(
        max_length=100,
        blank=False
    )
    location = models.CharField(
        max_length=100,
        blank=False
    )
    sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f'{self.artwork_title}'
