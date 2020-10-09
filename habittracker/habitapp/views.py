from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def test_view(request):
    data = {
        'First Name': 'Ichon',
        "Last Name": 'Kim'
    }
    return JsonResponse(data)

# class TestView(APIview):
#     def get(self, request, *args, **kwargs):
#     data = {
#         'First Name': 'Ichon',
#         "Last Name": 'Kim'
#     }
#     return JsonResponse(data)
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")