from rest_framework import serializers
from .models import Bid


class BidSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    is_buyer = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Bid
        fields = [
            'id', 'buyer', 'seller', 'artwork', 'bid_price', 'phone', 'email',
            'status', 'created_at', 'updated_at',
        ]
