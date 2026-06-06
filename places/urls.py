from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('place/<slug:slug>/', views.place_detail, name='place_detail'),
]
