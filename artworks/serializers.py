from rest_framework import serializers
from saves.models import Save
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    """
    Artwork model serializer. Validates image size, displays if the user is
    artwork's owner(boolean values), displays read-only bid count for the
    individual artwork.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    sold = serializers.BooleanField(default=False)
    bids_count = serializers.ReadOnlyField()
    save_id = serializers.SerializerMethodField()
    saved_count = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url'
    )

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

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, artwork=obj
            ).first()
            return save.id if save else None
        return None

    class Meta:
        model = Artwork
        fields = [
            'id', 'owner', 'owner_id', 'is_owner', 'artwork_title',
            'artist_name', 'description', 'style', 'type', 'payment_method',
            'price', 'image', 'contact', 'location', 'created_at',
            'updated_at', 'bids_count', 'save_id', 'saved_count', 'profile_id',
            'profile_image', 'sold'
        ]
