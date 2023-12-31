# Generated by Django 4.2 on 2023-12-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0022_cascadesservice_lightingservice_pavingservice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cascadesservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='cascadesservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cascadesservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cascadesservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='concreteservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='concreteservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='concreteservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='concreteservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='garageservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='garageservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='garageservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='garageservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lightingservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='lightingservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lightingservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lightingservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pavingservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='pavingservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pavingservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pavingservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantingservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantingservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantingservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantingservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='platformservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='platformservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='platformservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='platformservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poolservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='poolservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poolservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poolservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wallsservice',
            name='subtitle',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100),
        ),
        migrations.AlterField(
            model_name='wallsservice',
            name='subtitle_en',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wallsservice',
            name='subtitle_es',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wallsservice',
            name='subtitle_fr',
            field=models.CharField(blank=True, default='Text of Subtitle', max_length=100, null=True),
        ),
    ]
