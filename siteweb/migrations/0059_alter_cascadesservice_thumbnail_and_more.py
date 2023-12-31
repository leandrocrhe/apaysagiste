# Generated by Django 4.2 on 2024-01-07 04:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0058_alter_service_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cascadesservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='cascades_chimneys'),
        ),
        migrations.AlterField(
            model_name='concreteservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='concrete'),
        ),
        migrations.AlterField(
            model_name='garageservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='garage'),
        ),
        migrations.AlterField(
            model_name='home',
            name='background',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='home'),
        ),
        migrations.AlterField(
            model_name='lightingservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='lighting'),
        ),
        migrations.AlterField(
            model_name='pavingservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='pavers_asphalt'),
        ),
        migrations.AlterField(
            model_name='plantingservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='lawn_planting'),
        ),
        migrations.AlterField(
            model_name='platformservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='platform'),
        ),
        migrations.AlterField(
            model_name='poolservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='pool'),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='repair'),
        ),
        migrations.AlterField(
            model_name='wallsservice',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='walls'),
        ),
    ]
