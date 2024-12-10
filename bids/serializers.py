from rest_framework import serializers
from .models import Bid, STATUS
from artworks.models import Artwork


class BidSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    seller = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField()
    artwork_title = serializers.SerializerMethodField()

    def get_seller(self, obj):
        return obj.artwork.owner.username

    # def get_status(self, obj):
    #     return obj.artwork.sold

    def get_artwork_title(self, obj):
        return obj.artwork.artwork_title

    class Meta:
        model = Bid
        fields = [
            'id', 'buyer', 'seller', 'artwork_title', 'artwork', 'bid_price',
            'phone', 'email', 'status', 'created_at', 'updated_at'
        ]


class BidDetailSerializer(BidSerializer):
    artwork = serializers.ReadOnlyField(source='artwork.id')
    status = serializers.ChoiceField(choices=STATUS)

    # def get_owner(self, obj):
    #     return obj.buyer.owner.username
    
    class Meta:
        model = Bid
        fields = ['artwork','status']
