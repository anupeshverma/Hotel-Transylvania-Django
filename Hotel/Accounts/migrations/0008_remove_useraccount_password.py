# Generated by Django 4.2.1 on 2023-05-16 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='password',
        ),
    ]
