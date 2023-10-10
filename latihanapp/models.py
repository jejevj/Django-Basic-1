from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=225)
    completed = models.BooleanField(default=False)
    

class ListMahasiswa(models.Model):
    nama = models.CharField(max_length=200)
    kelas = models.CharField(max_length=20)
    nim = models.CharField(max_length=10)
    tgl_lahir = models.DateField()
    
    