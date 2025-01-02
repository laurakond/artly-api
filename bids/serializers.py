from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Bid, STATUS
from artworks.models import Artwork


class BidSerializer(serializers.ModelSerializer):
    """
    Bid model serializer. Fetches read-only buyer and seller fields, validates
    bid input value to be above 0.
    """
    buyer = serializers.ReadOnlyField(source='buyer.username')
    seller = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url'
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_seller(self, obj):
        return obj.artwork.owner.username

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate_bid_price(self, bid_price):
        if bid_price <= 0:
            raise serializers.ValidationError(
                "Invalid input. Please enter values above 0."
            )
        return bid_price

    class Meta:
        model = Bid
        fields = [
            'id', 'buyer', 'seller', 'artwork', 'bid_price',
            'email', 'status', 'profile_id', 'profile_image', 'created_at',
            'updated_at'
        ]


class BidDetailSerializer(BidSerializer):
    """
    Serializer for Bid detail view. Displays artwork id read-only, and
    fetches status choice field for the bid detail.
    """
    artwork = serializers.ReadOnlyField(source='artwork.id')
    status = serializers.ChoiceField(choices=STATUS)

    class Meta:
        model = Bid
        fields = ['artwork', 'status']
