# Generated by Django 4.2 on 2023-12-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0041_rename_about_about_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='long_text',
            field=models.TextField(default='A more long text'),
        ),
        migrations.AddField(
            model_name='about',
            name='long_text_en',
            field=models.TextField(default='A more long text', null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='long_text_es',
            field=models.TextField(default='A more long text', null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='long_text_fr',
            field=models.TextField(default='A more long text', null=True),
        ),
    ]