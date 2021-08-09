# Generated by Django 3.2.5 on 2021-07-30 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pr0001',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50, verbose_name='PROJE NO')),
                ('title2', models.CharField(max_length=50, verbose_name='PROJE ADI')),
                ('title3', models.CharField(max_length=50, verbose_name='MÜŞTERİ ADI')),
                ('title4', models.CharField(max_length=50, verbose_name='SİPARİŞ ADETİ')),
                ('title5', models.CharField(max_length=50, verbose_name='BAŞLAMA TARİHİ')),
                ('title6', models.CharField(max_length=50, verbose_name='BİTİŞ TARİHİ')),
                ('title7', models.CharField(max_length=50, verbose_name='PROJE SORUMLUSU')),
                ('title8', models.CharField(max_length=50, verbose_name='İRTİBAT NUMARASI')),
                ('content', models.TextField(verbose_name='AÇIKLAMA')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='OLUŞTURULMA TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='KULLANICI')),
            ],
        ),
    ]