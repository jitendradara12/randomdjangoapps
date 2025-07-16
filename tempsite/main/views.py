from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(responce, id):
    ls = models.ToDolist.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (ls, str(item.text)))
