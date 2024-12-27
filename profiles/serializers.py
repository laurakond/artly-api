from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Profile model serializer, fetches read-only owner field, artwork count,
    and sold artwork count.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    artwork_count = serializers.ReadOnlyField()
    sold_artwork_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'location', 'profile_image', 'styles',
            'techniques', 'influences', 'collaborations', 'portfolio_url',
            'artwork_count', 'sold_artwork_count', 'created_at', 'updated_at',
            'is_owner'
        ]
