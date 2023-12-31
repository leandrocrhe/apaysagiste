# Generated by Django 4.2 on 2023-12-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0024_alter_form_submit_alter_form_submit_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial', models.TextField()),
                ('client_name', models.CharField(max_length=50)),
                ('client_charge', models.CharField(default='client', max_length=50)),
                ('client_charge_en', models.CharField(default='client', max_length=50, null=True)),
                ('client_charge_fr', models.CharField(default='client', max_length=50, null=True)),
                ('client_charge_es', models.CharField(default='client', max_length=50, null=True)),
            ],
        ),
    ]
