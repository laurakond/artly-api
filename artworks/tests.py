from django.contrib.auth.models import User
from .models import Artwork
from rest_framework import status
from rest_framework.test import APITestCase


class ArtworkListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='name', password='password'
        )

    def test_can_list_artworks(self):
        name_test = User.objects.get(username='name')
        Artwork.objects.create(
            owner=self.user,
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
        response = self.client.get('/artworks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='name', password='password')
        response = self.client.post('/artworks/', {
            'artwork_title': 'artwork title',
            'description': 'artwork description',
            'style': 'Other',
            'type': 'Other',
            'payment_method': 'Cash',
            'price': 20.00,
            'contact': 'email@email.com',
            'location': 'somewhere',
            'sold': False,
        })
        count = Artwork.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/artworks/', {
            'artwork_title': 'artwork title',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
