# Generated by Django 4.2 on 2023-12-11 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0034_bannerpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerpage',
            name='banner',
        ),
    ]