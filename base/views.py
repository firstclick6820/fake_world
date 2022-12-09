from django.shortcuts import render


# Import Requsts
from django.http import FileResponse,HttpResponse, JsonResponse


# Imoprt Json
import json


from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions


from faker import Faker



# As we user Faker in our views, we will create a global variable for it
faker = Faker()


# ====================================================== Home View =========================================

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    
    context = {
        "Home Page": "Faker API is used to generate Fake Information.",
        "URLS" : {
            "Fake Names" :   "/names/10/",
            "Fake Address": "/address/10/",
            "Fake Country": "/country/10/",
            "Fake City": '/city/10/'
        },
    }
    return JsonResponse(context, safe=False)





#  ==================================================== Fake Names API ================================================

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fake_names(request, to_range = int):
    
    limit = int
    result = []
    
    if to_range and type(to_range) == int and to_range > 0:
        limit = to_range 
        
   
        
    for _ in range(0, limit):
        result.append(faker.name())
        
    context = {
        "Data": result
    }
        
    return JsonResponse(context, safe=False)
        
        
        
        
#=========================================================== Fake Address =========================================
    
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fake_address(request, to_range = int):
    
    limit = int
    result = []
    
    if to_range and type(to_range) == int and to_range > 0:
        limit = to_range 
        
   
        
    for _ in range(0, limit):
        result.append(faker.address())
        
    context = {
        "Data": result
    }
        
    return JsonResponse(context, safe=False)



# Country 
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fake_countries(request, to_range = int):
    
    limit = int
    result = []
    
    if to_range and type(to_range) == int and to_range > 0:
        limit = to_range 
        
   
        
    for _ in range(0, limit):
        result.append(faker.country())
        
    context = {
        "Data": result
    }
        
    return JsonResponse(context, safe=False)



# City 
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def fake_cities(request, to_range = int):
    
    limit = int
    result = []
    
    if to_range and type(to_range) == int and to_range > 0:
        limit = to_range 
        
   
        
    for _ in range(0, limit):
        result.append(faker.city())
        
    context = {
        "Data": result
    }
        
    return JsonResponse(context, safe=False)
