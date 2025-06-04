from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='Contact'),
    path('tracker/',views.tracker,name='TrckingStatus'),
    path('search/',views.search,name='Search'),
    path('productview/',views.productview,name='ProdView'),
    path('checkout/',views.checkout,name='Checkout'),
]
