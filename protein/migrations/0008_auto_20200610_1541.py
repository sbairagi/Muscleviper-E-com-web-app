# Generated by Django 3.0.4 on 2020-06-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='product_title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]