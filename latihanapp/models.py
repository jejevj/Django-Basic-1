from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=225)
    diskon = models.BooleanField(default=False)
    

class ListMahasiswa(models.Model):
    nama = models.CharField(max_length=200)
    kelas = models.CharField(max_length=20)
    nim = models.CharField(max_length=10)
    tgl_lahir = models.DateField()
    
    
class ProdukItem(models.Model):
    nama_produk = models.CharField(max_length=200)
    harga = models.CharField(max_length=100)
    

class BuahItem(models.Model):
    nama_buah = models.CharField(max_length=200)
    harga = models.CharField(max_length=100)
        