# Generated by Django 4.2.1 on 2023-05-31 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0015_wine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='alcohols',
            new_name='alcohol',
        ),
    ]
