from django.db import IntegrityError
from rest_framework import serializers
from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model
    The create method handles the unique constraint on 'owner' and 'artwork'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = ['id', 'created_at', 'owner', 'artwork']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible dupblicate'
            })
