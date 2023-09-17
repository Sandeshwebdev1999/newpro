# Generated by Django 4.1.5 on 2023-03-08 03:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0015_coupon_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealsproduct',
            name='Discount',
        ),
        migrations.CreateModel(
            name='Recommended_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField()),
                ('Availibility', models.IntegerField()),
                ('feature_image', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('product_information', ckeditor.fields.RichTextField()),
                ('model_name', models.CharField(max_length=100)),
                ('Tags', models.CharField(max_length=100)),
                ('Description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, default='', max_length=500, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app4.brand')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.category')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app4.color')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app4.section')),
            ],
        ),
    ]
