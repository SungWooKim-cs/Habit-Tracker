from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render


# third party imports
# from rest_framework.response import Response
# from rest_framework.views import APIView
# import requests
# import json

from .forms import LoginForm

def login_form(request):
    username = 'Mikelover'
    password = 'Sungsim'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['username'] == username and form.cleaned_data['password'] == password: 
                message = 'Hello, you\'re logged in!'
                return render(request, 'habitapp/login_response.html', {'message': message})
            else:
                message = 'Sorry, you\'re not able to log in...'
                return render(request, 'habitapp/login_response.html', {'message': message})
                
    else:
        form = LoginForm()

    return render(request, 'habitapp/login.html', {'form': form})

# Create your views here.
def login(request):
    return render(request, 'habitapp/login.html')

# class TestView(APIview):
#     def get(self, request, *args, **kwargs):
#     data = {
#         'First Name': 'Ichon',
#         "Last Name": 'Kim'
#     }
#     return JsonResponse(data)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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