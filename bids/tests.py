from django.contrib.auth.models import User
from .models import Bid, Artwork
from rest_framework import status
from rest_framework.test import APITestCase
from .views import BidList


class BidListViewTests(APITestCase):
    """
    Test to check if the user can create a bid instance, list them, and
    cannot create artwork if they are loggged out.
    """
    def setUp(self):
        self.user_one = User.objects.create_user(
            username='buyer', password='password'
        )
        self.user_two = User.objects.create_user(
            username='seller', password='password'
        )
        self.artwork = Artwork.objects.create(
            owner=self.user_two,
            artwork_title='artwork title',
            description='artwork description',
            style='Other',
            type='Other',
            payment_method='Cash',
            price=20,
            contact='email@email.com',
            location='somewhere',
            sold=False,
        )

    def test_can_list_bid(self):
        """test to check that a list of bids is created."""
        name_test = User.objects.get(username='seller')
        Bid.objects.create(
            buyer=self.user_one,
            seller=self.artwork.owner,
            artwork=self.artwork,
            bid_price=self.artwork.price,
            email='buyer@email.com',
            status='Pending'
        )
        response = self.client.get('/bids/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_bid_with_correct_value(self):
        """
        test to check that the buyer can create a bid with the right bid price.
        """
        self.client.login(username='buyer', password='password')
        response = self.client.post('/bids/', {
            'artwork': self.artwork.id,
            'bid_price': 20.00,
            'email': 'buyer@email.com',
            'status': 'Pending'
        })
        count = Bid.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_bid(self):
        """test to check that the user cannot create a bid when logged out."""
        response = self.client.post('/bids/', {
            'artwork': self.artwork.id,
            'bid_price': 10.00,
            'email': 'buyer@email.com',
            'status': 'Pending'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_zero_value_bid_input(self):
        """test to check if the bid price is denied at 0."""
        self.client.login(username='buyer', password='password')
        response = self.client.post('/bids/', {
            'artwork': self.artwork.id,
            'bid_price': 00.00,
            'email': 'buyer@email.com',
            'status': 'Pending'
        })
        count = Bid.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_value_bid_input(self):
        """test to check if the bid price is denied at negative value."""
        self.client.login(username='buyer', password='password')
        response = self.client.post('/bids/', {
            'artwork': self.artwork.id,
            'bid_price': -1.00,
            'email': 'buyer@email.com',
            'status': 'Pending'
        })
        count = Bid.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
