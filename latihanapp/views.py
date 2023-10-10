from django.shortcuts import render, HttpResponse
from .models import *


def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html",{ "todos":items })

def listMahasiswa(request):
    items = ListMahasiswa.objects.all()
    return render(request, 'listMahasiswa.html', {"mahasiswa":items})

def produk(request):
    items = ProdukItem.objects.all()
    return render(request, 'produk.html', {"produk":items})