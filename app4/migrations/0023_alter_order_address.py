# Generated by Django 4.1.5 on 2023-03-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0022_rename_total_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=100),
        ),
    ]