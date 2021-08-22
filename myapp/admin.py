from django.contrib import admin
from .models import Activities ,Excursions , Admin ,Images,Traget ,CartProduct ,Cart ,  Order , HotelAdmin

# Register your models here.

admin.site.register([Activities , Excursions ,Admin ,Images , Traget , CartProduct , Cart , Order,HotelAdmin ])
