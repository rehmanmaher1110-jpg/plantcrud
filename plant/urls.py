from django.urls import path
from .views import plant_home

urlpatterns = [
    path('', plant_home, name='plant_home'),
]