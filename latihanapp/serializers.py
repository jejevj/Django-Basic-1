from .models import *
from rest_framework import serializers as sz

class MatakuliahSerializer(sz.ModelSerializer):
    class Meta:
        model = matakuliah
        fields = '__all__'