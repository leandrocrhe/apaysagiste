# Generated by Django 4.2 on 2023-12-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0047_home_testimonials_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='testimonials_title_en',
            field=models.CharField(default='Testimonials', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='testimonials_title_es',
            field=models.CharField(default='Testimonials', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='testimonials_title_fr',
            field=models.CharField(default='Testimonials', max_length=50, null=True),
        ),
    ]