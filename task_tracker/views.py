from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def tasks(request):
    tasks = Task.objects.all()
    return JsonResponse([task.serialize() for task in tasks], safe=False)