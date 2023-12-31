from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    
    path('todos/',views.todos,name="Todos"),
    
    path('mahasiswa/',views.listMahasiswa,name="List Mahasiswa"),
    
    path('produk/',views.produk,name="Daftar Produk"),
    
    path('buah/',views.buah,name="Daftar Buah"),
    
    path('konten/',views.konten,name="Daftar Konten"),
    
    path('blog/',views.blog,name="Daftar Blog"),
    
    path('matkul/',views.matkul,name="Daftar Blog"),
    
    path('api-matkul',views.getMatkul),
    path('api/store-matkul',views.MatkulCreateView.as_view(), name='matkul-create'),
]