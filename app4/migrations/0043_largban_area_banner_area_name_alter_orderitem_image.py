# Generated by Django 4.1.5 on 2023-04-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0042_remove_smartphone_image_smartphone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='largban_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/largban_img')),
                ('Discount_Deal', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='banner_area',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(upload_to='media/order_images'),
        ),
    ]
