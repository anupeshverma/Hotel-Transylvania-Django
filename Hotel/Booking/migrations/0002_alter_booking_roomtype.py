# Generated by Django 4.2.1 on 2023-08-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='roomType',
            field=models.CharField(default='General', max_length=20),
        ),
    ]
