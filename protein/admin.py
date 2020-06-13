from django.contrib import admin
from .models import Brands,Brandimage,Contact,Order
# Register your models here.


admin.site.register(( Brands, Brandimage,Contact,Order))