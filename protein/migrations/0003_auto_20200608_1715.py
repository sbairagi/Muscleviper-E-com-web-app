# Generated by Django 3.0.4 on 2020-06-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0002_auto_20200608_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='product_imgurl1',
            field=models.URLField(blank=True, default='', verbose_name='PRODUCT IMAGE URL1'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='product_imgurl2',
            field=models.URLField(blank=True, default='', verbose_name='PRODUCT IMAGE URL2'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='product_imgurl3',
            field=models.URLField(blank=True, default='', verbose_name='PRODUCT IMAGE URL3'),
        ),
    ]
