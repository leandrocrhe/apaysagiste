# Generated by Django 4.2 on 2023-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0012_remove_service_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_fr',
            field=models.TextField(blank=True, null=True),
        ),
    ]
