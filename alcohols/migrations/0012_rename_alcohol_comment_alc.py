# Generated by Django 4.2.1 on 2023-05-31 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0011_rename_wines_wine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='alcohol',
            new_name='alc',
        ),
    ]
