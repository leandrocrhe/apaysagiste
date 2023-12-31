# Generated by Django 4.2 on 2023-12-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0030_remove_gallery_height_remove_gallery_width'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='banner')),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='banner',
            field=models.ImageField(default='Required', upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_en',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_es',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_fr',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(default='Service', max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_en',
            field=models.CharField(default='Service', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_es',
            field=models.CharField(default='Service', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_fr',
            field=models.CharField(default='Service', max_length=50, null=True),
        ),
    ]
