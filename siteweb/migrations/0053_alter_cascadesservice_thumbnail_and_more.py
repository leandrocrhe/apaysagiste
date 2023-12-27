# Generated by Django 4.2 on 2023-12-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0052_contact_link_facebook_contact_link_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cascadesservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/cascades_chimneys'),
        ),
        migrations.AlterField(
            model_name='concreteservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/concrete'),
        ),
        migrations.AlterField(
            model_name='garageservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/garage'),
        ),
        migrations.AlterField(
            model_name='lightingservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/lighting'),
        ),
        migrations.AlterField(
            model_name='pavingservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/pavers_asphalt'),
        ),
        migrations.AlterField(
            model_name='plantingservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/lawn_planting'),
        ),
        migrations.AlterField(
            model_name='platformservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/platform'),
        ),
        migrations.AlterField(
            model_name='poolservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/pool'),
        ),
        migrations.AlterField(
            model_name='repairservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/repair'),
        ),
        migrations.AlterField(
            model_name='wallsservice',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='services/walls'),
        ),
    ]