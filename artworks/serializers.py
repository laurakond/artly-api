from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    sold = serializers.ReadOnlyField()

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
