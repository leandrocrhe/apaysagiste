# Generated by Django 4.2 on 2023-12-13 17:06

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0043_remove_about_text_remove_about_text_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='images',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='about'),
        ),
    ]
