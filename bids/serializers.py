from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Bid, STATUS
from artworks.models import Artwork


class BidSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    seller = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField()
    # artwork_title = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_seller(self, obj):
        return obj.artwork.owner.username

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    # def get_artwork_title(self, obj):
    #     return obj.artwork.artwork_title

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
            'email', 'status', 'created_at', 'updated_at'
        ]


class BidDetailSerializer(BidSerializer):
    artwork = serializers.ReadOnlyField(source='artwork.id')
    status = serializers.ChoiceField(choices=STATUS)

    class Meta:
        model = Bid
        fields = ['artwork', 'status']
