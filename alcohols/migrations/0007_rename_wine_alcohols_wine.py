# Generated by Django 4.2.1 on 2023-05-31 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0006_wine'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wine',
            new_name='alcohols_wine',
        ),
    ]