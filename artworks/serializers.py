from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    sold = serializers.ReadOnlyField()

    # validate_image function has been taken from the Code Institute DRF API
    # walkthrough.
    def validate_image(self, value):
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
            'id', 'owner', 'artwork_title', 'artist_name', 'description',
            'style', 'type', 'payment_method', 'price', 'image', 'alt_text',
            'contact', 'location', 'sold', 'created_at', 'updated_at',
            'is_owner', 'owner_id'
        ]
