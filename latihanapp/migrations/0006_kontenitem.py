# Generated by Django 4.2.6 on 2023-10-11 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latihanapp', '0005_buahitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='KontenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('konten', models.CharField(max_length=2000)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]