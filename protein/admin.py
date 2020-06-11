from django.contrib import admin
from .models import Brands,Brandimage,Contact
# Register your models here.


admin.site.register(( Brands, Brandimage,Contact))