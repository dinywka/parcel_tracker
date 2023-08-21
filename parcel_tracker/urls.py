from django.urls import path
from parcel_tracker import views

urlpatterns = [
    path('', views.home, name="home"),
    path('price/', views.price, name="price")
]