# Generated by Django 4.2 on 2023-12-14 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0048_home_testimonials_title_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='tercer_title',
            new_name='third_title',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='tercer_title_en',
            new_name='third_title_en',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='tercer_title_es',
            new_name='third_title_es',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='tercer_title_fr',
            new_name='third_title_fr',
        ),
    ]
