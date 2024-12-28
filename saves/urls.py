from django.urls import path
from saves import views

urlpatterns = [
  path('saved/', views.SaveList.as_view()),
  path('saved/<int:pk>', views.SaveDetail.as_view()),
]
