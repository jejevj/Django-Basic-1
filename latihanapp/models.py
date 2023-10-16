from django.db import models
from tinymce.models import HTMLField  

# Create your models here.
from django import forms 
from tinymce.widgets import TinyMCE 
  
class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False
  
  
class PostForm(forms.ModelForm): 
    content = forms.CharField( 
        widget=TinyMCEWidget( 
            attrs={'required': False, 'cols': 30, 'rows': 10} 
        ) 
    ) 
    # class Meta: 
    #     model = models 
    #     fields = '__all__'
        
        
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
    

class KontenItem(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.CharField(max_length=2000)
    created_at = models.DateField(auto_now=True)
        
    
class article(models.Model): 
    judul = models.CharField(max_length=200)
    content =  HTMLField()   
    created_at = models.DateField(auto_now=True)  
    

    
class matakuliah(models.Model): 
    kode_mata_kuliah = models.CharField(max_length=10)
    nama_mata_kuliah = models.CharField(max_length=100)
    sks = models.CharField(max_length=1)
    # content =  HTMLField()   
    created_at = models.DateField(auto_now=True)  