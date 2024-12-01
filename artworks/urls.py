from django.urls import path
from artworks import views

urlpatterns = [
    path('artworks/', views.ArtworkList.as_view()),
]