# Generated by Django 4.2 on 2023-12-02 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0018_service_1_description_en_service_1_description_es_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_1',
            new_name='ConcreteService',
        ),
    ]