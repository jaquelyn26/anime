from django.urls import path
from .views import *


urlpatterns = [
    path('', Mascotas, name='Mascotas'),
    path('furnitures/', anime, name='furnitures'),
    path('contact/', anime, name='contact'),
    path('company/', anime, name='company'),
    path('about/', anime, name='about'),
]
