from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    sold = serializers.BooleanField(default=False)

    def validate_image(self, value):
        """
        Function to validate a certain image size upon upload. This function
        code has been taken from the Code Institute DRF API walkthrough.
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image larger than 2MB.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Artwork
        fields = [
            'id', 'owner', 'owner_id', 'is_owner', 'artwork_title',
            'artist_name', 'description', 'style', 'type', 'payment_method',
            'price', 'image', 'alt_text', 'contact', 'location', 'created_at',
            'updated_at',  'sold'            
        ]
