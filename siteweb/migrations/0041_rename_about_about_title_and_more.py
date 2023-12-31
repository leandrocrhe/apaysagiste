# Generated by Django 4.2 on 2023-12-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0040_service_identificador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='about_en',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='about_es',
            new_name='title_es',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='about_fr',
            new_name='title_fr',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_text',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_text_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_text_es',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_text_fr',
        ),
        migrations.AddField(
            model_name='about',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='about'),
        ),
        migrations.AddField(
            model_name='about',
            name='subtitle',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='subtitle_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='subtitle_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='subtitle_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='text',
            field=models.TextField(default='text of this section'),
        ),
        migrations.AddField(
            model_name='about',
            name='text_en',
            field=models.TextField(default='text of this section', null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='text_es',
            field=models.TextField(default='text of this section', null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='text_fr',
            field=models.TextField(default='text of this section', null=True),
        ),
    ]
