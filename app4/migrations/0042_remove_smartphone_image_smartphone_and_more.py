# Generated by Django 4.1.5 on 2023-04-07 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0041_rename_feature_image_smartphone_phone_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone_image',
            name='smartphone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='smartphone',
        ),
        migrations.DeleteModel(
            name='SmartPhone',
        ),
        migrations.DeleteModel(
            name='SmartPhone_Image',
        ),
    ]
