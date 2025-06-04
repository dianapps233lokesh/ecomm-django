from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='BlogHome'),
    # path('shop/',include('shop.urls')),
]
