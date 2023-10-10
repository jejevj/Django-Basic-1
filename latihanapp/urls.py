from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('todos/',views.todos,name="Todos"),
    
    path('mahasiswa/',views.listMahasiswa,name="List Mahasiswa"),
    
    path('produk/',views.produk,name="Daftar Produk")
]