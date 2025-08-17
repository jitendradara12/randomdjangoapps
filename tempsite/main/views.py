from django.shortcuts import render
from . import models
# Create your views here.


def index(responce, id):
    return render(responce, 'main/base.html',{})


def home(responce):
    return render(responce, "main/home.html", {})


def list(responce):
    ls = models.ToDolist.objects.get(id=1)
    return render(responce, "main/list.html", {"ls":ls})
