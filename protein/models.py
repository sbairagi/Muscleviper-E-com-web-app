from django.db import models

# Create your models here.

CATEGORIES = (  
    ('weight loss', 'weight loss'),
    ('daily vitals', 'daily vitals'),
    ('mass gainers', 'mass gainers'),
)

TRANDING = (  
    ('YES', 'YES'),
    ('NO', 'NO'),
)



brand = (  
    ('apple', 'apple'),
    ('samsung', 'samsung'),
    ('lg', 'lg'),
    ('mi', 'mi'),
    ('nokia', 'nokia'),
    ('vivo', 'vivo'),
    ('jio', 'jio'),
    ('opo', 'opo'),
)

class Brands(models.Model):
    bsno = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=255,unique=True)
    tranding_product = models.CharField(max_length=10,choices=TRANDING)
    product_desc = models.TextField()
    product_brand = models.CharField(max_length=255,choices=brand)
    product_imgurl = models.CharField("PRODUCT IMAGE URL", max_length=255)
    product_imgurl1 = models.CharField("PRODUCT IMAGE URL1", max_length=255, blank=True, default="")
    product_imgurl2 = models.CharField("PRODUCT IMAGE URL2", max_length=255, blank=True, default="")
    product_imgurl3 = models.CharField("PRODUCT IMAGE URL3", max_length=255, blank=True, default="")
    product_price = models.IntegerField()
    product_percent_off = models.IntegerField(default=00)
    product_weight = models.CharField( max_length=20,default=0)
    product_category = models.CharField(max_length=20,choices=CATEGORIES)

    def __str__(self):
        return self.product_category + " " + self.product_title


brand = (  
    ('apple', 'apple'),
    ('samsung', 'samsung'),
    ('lg', 'lg'),
    ('mi', 'mi'),
    ('nokia', 'nokia'),
    ('vivo', 'vivo'),
    ('jio', 'jio'),
    ('opo', 'opo'),
)



class Brandimage(models.Model):
    bisno = models.AutoField(primary_key=True)
    brand_imgurl = models.URLField("BRAND IMAGE URL")
    brand_logourl = models.URLField("BRAND LOGO URL")
    brand_name = models.CharField(max_length=255,choices=brand)

    def __str__(self):
        return self.brand_name

class Contact(models.Model):
    csno = models.AutoField(primary_key=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


class Order(models.Model):
    itemsJson = models.TextField()
    amount = models.IntegerField()
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    email = models.EmailField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=30)
    zip_code = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.email

