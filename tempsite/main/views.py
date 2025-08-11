from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(responce, id):
    ls = models.ToDolist.objects.get(id=id)
    return render(responce, 'main/base.html', {})


def home(responce):
    return render(responce, "main/home.html", {})
