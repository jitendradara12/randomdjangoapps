from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models, forms
# Create your views here.


def index(responce, id):
    return render(responce, 'main/base.html', {})


def home(responce):
    return render(responce, "main/home.html", {})


def list(responce, id):
    ls = models.ToDolist.objects.get(id=id)
    if responce.method == 'POST':
        print(responce.POST)
        if responce.POST.get("save"):
            for item in ls.item_set.all():
                if responce.POST.get('c'+str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif responce.POST.get("NewItem"):
            pass

    return render(responce, "main/list.html", {"ls": ls})


def create(responce):

    if responce.method == "POST":
        form = forms.NewToDolist(responce.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = models.ToDolist(name=n)
            t.save()
        HttpResponseRedirect("main/%i" % t.id)
    else:
        form = forms.NewToDolist()

    return render(responce, "main/create.html", {"form": form})
