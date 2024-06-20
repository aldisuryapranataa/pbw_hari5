from django.db import models
from django import forms
from datetime import date
from django.utils import timezone



# Create your models here.
class Pengguna (models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address_1 = models.TextField()
    address_2  = models.TextField(null=True, blank = True)
    city = models.CharField(max_length=20, help_text='Enter your city')
    state= models.TextField()
    zip_code= models.CharField(max_length = 7)
    tanggal_join = models.DateField(auto_now = True)
    def __str__(self):
        return f'{self.email}' 
    

class Content(models.Model):
    author = models.ForeignKey(Pengguna, on_delete = models.CASCADE)
    date_created = models.DateField(auto_now = True)
    artikel = models.TextField()
    set_view = models.BooleanField(default=False)
    
from django.db import models

class Kelompok(models.Model):
    DESKRIPSI_CHOICES = [
        ('Deskripsi fitur', 'Deskripsi fitur'),
        ('Deskripsi label', 'Deskripsi label'),
    ]
    KATEGORI_CHOICES = [
        ('klasifikasi', 'Klasifikasi'),
        ('prediksi_numerik', 'Prediksi Numerik'),
        ('prediksi_probabilistik', 'Prediksi Probabilistik'),
        ('deteksi', 'Deteksi'),
        ('rekognisi', 'Rekognisi'),
    ]
    STATUS_CHOICES = [
        ('selesai', 'Selesai'),
        ('berlangsung', 'Berlangsung'),
        ('gagal', 'Gagal'),
    ]

    deskripsi = models.CharField(max_length=100, choices=DESKRIPSI_CHOICES)
    sub_deskripsi = models.CharField(max_length=200, blank=True, null=True)
    kategori = models.CharField(max_length=30, choices=KATEGORI_CHOICES)
    tanggal_mulai_pemodelan = models.DateField()
    tanggal_selesai_pemodelan = models.DateField()
    status_penyelesaian = models.CharField(max_length=20, choices=STATUS_CHOICES)
        
    def __str__(self):
        return self.deskripsi

class Kelompok(models.Model):
    DESKRIPSI_CHOICES = [
        ('Deskripsi fitur', 'Deskripsi fitur'),
        ('Deskripsi label', 'Deskripsi label'),
    ]
    KATEGORI_CHOICES = [
        ('klasifikasi', 'Klasifikasi'),
        ('prediksi_numerik', 'Prediksi Numerik'),
        ('prediksi_probabilistik', 'Prediksi Probabilistik'),
        ('deteksi', 'Deteksi'),
        ('rekognisi', 'Rekognisi'),
    ]
    STATUS_CHOICES = [
        ('selesai', 'Selesai'),
        ('berlangsung', 'Berlangsung'),
        ('gagal', 'Gagal'),
    ]

    deskripsi = models.CharField(max_length=100, choices=DESKRIPSI_CHOICES)
    sub_deskripsi = models.CharField(max_length=200, blank=True, null=True)
    kategori = models.CharField(max_length=30, choices=KATEGORI_CHOICES)
    tanggal_mulai_pemodelan = models.DateField()
    tanggal_selesai_pemodelan = models.DateField()
    status_penyelesaian = models.CharField(max_length=20, choices=STATUS_CHOICES)
        
    def __str__(self):
        return self.deskripsi

class Icreation(models.Model):
    CATEGORY_CHOICES = [
        ('Klasifikasi', 'Klasifikasi'),
        ('Prediksi Numerik', 'Prediksi Numerik'),
        ('Prediksi Probabilistik', 'Prediksi Probabilistik'),
        ('Deteksi', 'Deteksi'),
        ('Rekognisi', 'Rekognisi'),
    ]

    STATUS_CHOICES = [
        ('Selesai', 'Selesai'),
        ('Berlangsung', 'Berlangsung'),
        ('Gagal', 'Gagal'),
    ]

    deskripsi_masalah = models.TextField(default='')
    deskripsi_fitur = models.TextField(default='')
    deskripsi_label = models.TextField(default='')
    kategori_masalah = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Klasifikasi')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status_penyelesaian = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Selesai')
    catatan_akhir = models.TextField(blank=True, null=True)
    waktu_perekaman = models.DateTimeField(default=timezone.now, blank=True)  # Tambahkan default di sini
    waktu_update_terakhir = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deskripsi_masalah



    
    

# Create your models here.
