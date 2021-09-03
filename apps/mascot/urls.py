from django.urls import path
from .views import *


urlpatterns = [
    path('', Mascotas, name='Mascotas'),
    path('anime/', anime, name='anime'),
]
