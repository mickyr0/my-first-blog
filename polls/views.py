from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# http://localhost:8000/pollsを開く
def index(request):
    print(1)
    print(2)
    print(3)
    return HttpResponse("Hello, world. You're at the polls index.")

