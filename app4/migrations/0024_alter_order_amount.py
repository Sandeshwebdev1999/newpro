# Generated by Django 4.1.5 on 2023-03-11 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0023_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
