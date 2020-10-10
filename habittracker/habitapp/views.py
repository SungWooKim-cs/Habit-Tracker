from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'habitapp/login.html')


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def test_view(request):
    data = {
        'name': 'Jiyun',
        'age': 26
    }
    return JsonResponse(data)

def test_login(request):
    login = [
        {'id' : 'ilsannoh',
        'password' : 'sanbonkim'}
    ]

    return JsonResponse({'login' : login})

r = requests.get('https://www.python.org')