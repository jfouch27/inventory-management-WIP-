# Generated by Django 3.2.7 on 2021-10-12 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OpenPorts',
            new_name='OpenPort',
        ),
    ]
