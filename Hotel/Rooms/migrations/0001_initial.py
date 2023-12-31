# Generated by Django 4.2.1 on 2023-08-16 10:50

import Rooms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomNo', models.IntegerField(primary_key=True, serialize=False)),
                ('roomType', models.CharField(choices=[('General', 'General'), ('Special', 'Special')], default='general', max_length=20, verbose_name='Room Type')),
                ('capacity', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Triple', 'Triple')], max_length=20, verbose_name='Capacity')),
                ('price', models.FloatField()),
                ('roomImage', models.ImageField(upload_to=Rooms.models.room_image_path)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
