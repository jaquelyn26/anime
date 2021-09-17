from django.urls import path
from .views import *


urlpatterns = [
    path('', Mascotas, name='mascotas'),
    path('furnitures/', anime, name='furnitures'),
    path('contact/', jaq, name='contact'),
    path('about/', chormi, name='about'),
]
