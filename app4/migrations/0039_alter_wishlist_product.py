# Generated by Django 4.1.5 on 2023-03-31 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0038_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(to='app4.product'),
        ),
    ]