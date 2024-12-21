from django.contrib.auth.models import User
from .models import Artwork
from rest_framework import status
from rest_framework.test import APITestCase

# Below tests have been based on Code Institute's DRF API walkthrough project.

class ArtworkListViewTests(APITestCase):
    """
    Test to check if the user can create the artwork instance, list them, and
    cannot create artwork if they are loggged out.
    """
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

    def test_logged_in_user_can_create_artwork(self):
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

    def test_logged_out_user_cannot_create_artworks(self):
        response = self.client.post('/artworks/', {
            'artwork_title': 'artwork title',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class ArtworksDetailViewTests(APITestCase):
#     def setUp(self):
#         self.user_one = User.objects.create_user(
#             username='user_one',
#             password='password'
#         )
#         self.user_two = User.objects.create_user(
#             username='user_two',
#             password='password2'
#         )
#         Artwork.objects.create(
#             owner=self.user_one,
#             artwork_title='artwork title 1',
#             description='artwork description 1',
#             style='Other',
#             type='Other',
#             payment_method='Cash',
#             price=20,
#             contact='user1@email.com',
#             location='user1',
#             sold=False,
#         )
#         Artwork.objects.create(
#             owner=self.user_two,
#             artwork_title='artwork title 2',
#             description='artwork description 2',
#             style='Modern',
#             type='Painting',
#             payment_method='Cash',
#             price=20,
#             contact='user2@email.com',
#             location='user2',
#             sold=False,
#         )

#     def test_can_retrieve_artwork_using_valid_id(self):
#         response = self.client.get('/artworks/1/')
#         self.assertEqual(response.data[
#             'artwork_title'
#         ], 'artwork title 1')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cannot_retrieve_artwork_by_invalid_id(self):
#         response = self.client.get('/artworks/100/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_owned_artwork(self):
#         self.client.login(username='user_one', password='password')
#         response = self.client.put(
#             '/artworks/1/',
#             {
#                 'artwork_title': 'edit user one artwork title',
#                 'description': 'artwork description',
#                 'style': 'Other',
#                 'type': 'Other',
#                 'payment_method': 'Cash',
#                 'price': 20.00,
#                 'contact': 'user1@email.com',
#                 'location': 'user1',
#                 'sold': False,
#             }
#         )
#         artwork = Artwork.objects.filter(pk=1).first()
#         self.assertEqual(artwork.artwork_title, 'edit user one artwork title')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cannot_update_others_artwork(self):
#         self.client.login(username='user_one', password='password')
#         response = self.client.put(
#             '/artworks/2/',
#             {'artwork_title': 'a new title'}
#         )
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
