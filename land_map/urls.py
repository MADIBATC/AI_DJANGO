from django.urls import path
from .views import *

app_name = 'land_map'

urlpatterns = [
    path('land-map/', landMap, name='map')
]
