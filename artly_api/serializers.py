from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


# This code was appropriated from Code Institute's DRF_API walkthrough project.
class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.images.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
