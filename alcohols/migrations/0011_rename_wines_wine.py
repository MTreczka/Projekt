# Generated by Django 4.2.1 on 2023-05-31 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0010_alter_wines_color_alter_wines_dryness'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wines',
            new_name='Wine',
        ),
    ]