# Generated by Django 4.2 on 2023-04-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0005_alter_form_postal_code_alter_form_postal_code_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='tercer_title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='form',
            name='tercer_title_en',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='tercer_title_es',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='tercer_title_fr',
            field=models.CharField(max_length=60, null=True),
        ),
    ]