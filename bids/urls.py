from django.urls import path
from bids import views

urlpatterns = [
    path('bids/', views.BidList.as_view()),
    path('bids/<int:pk>/', views.BidDetail.as_view()),
]