from django.urls import path, re_path

from . views import (
    
    home,
    fake_names,
    fake_address,
    fake_countries,
    fake_cities
)



urlpatterns = [
    path('', home, name='home Page'),
    path('names/<int:to_range>/', fake_names, name="names"),
    path('address/<int:to_range>/', fake_address, name="address"),
    path('country/<int:to_range>/', fake_countries, name="country"),
    path('city/<int:to_range>/', fake_cities, name ='fake_cities')
]
