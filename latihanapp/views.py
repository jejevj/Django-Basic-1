from django.shortcuts import render, HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers


class MatakuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = matakuliah
        fields = '__all__'

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


def buah(request):
    items = BuahItem.objects.all()
    return render(request, 'buah.html', {"buah":items})


def konten(request):
    items = KontenItem.objects.all()
    return render(request, 'konten.html', {"konten":items})


def blog(request):
    items = article.objects.all()
    return render(request, 'detail.html', {"konten":items})


def matkul(request):
    items = matakuliah.objects.all()
    return render(request, 'matkul.html', {"konten":items})


@api_view(['GET'])
def getMatkul(request):
    matkul = matakuliah.objects.all()
    serializer = MatakuliahSerializer(matkul, many=True)
    return Response(serializer.data)