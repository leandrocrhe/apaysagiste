# Generated by Django 4.2 on 2023-12-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0031_bannerpage_alter_service_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerpage',
            name='banner_en',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='bannerpage',
            name='banner_es',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
        migrations.AddField(
            model_name='bannerpage',
            name='banner_fr',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
    ]