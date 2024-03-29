# Generated by Django 4.2 on 2024-01-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0062_alter_servicelocation_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelocation',
            name='text',
            field=models.CharField(default='Landscaping expert in downtown Quebec City', max_length=80),
        ),
        migrations.AlterField(
            model_name='servicelocation',
            name='text_en',
            field=models.CharField(default='Landscaping expert in downtown Quebec City', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='servicelocation',
            name='text_es',
            field=models.CharField(default='Landscaping expert in downtown Quebec City', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='servicelocation',
            name='text_fr',
            field=models.CharField(default='Landscaping expert in downtown Quebec City', max_length=80, null=True),
        ),
    ]
