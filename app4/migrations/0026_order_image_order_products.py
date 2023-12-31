# Generated by Django 4.1.5 on 2023-03-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0025_rename_city_order_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(null=True, upload_to='accounts/order/image'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
