import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def tasks(request):
    tasks = Task.objects.all()
    return JsonResponse([task.serialize() for task in tasks], safe=False)

@csrf_exempt
def new_task(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    data = json.loads(request.body)
    text = data.get("text", "")
    day = data.get("day", "")
    reminder = data.get("reminder", "")

    Task(text=text, day=day, reminder=reminder).save()
    return JsonResponse({"message": "Task was added successfully"}, status=201)

@csrf_exempt
def reminder(request, task_id):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required"}, status=400)
    
    task = Task.objects.get(id=task_id)
    data = json.loads(request.body)
    task.reminder = data.get("reminder", "")
    task.save()
    return HttpResponse(status=204)