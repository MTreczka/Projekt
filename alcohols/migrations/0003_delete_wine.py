# Generated by Django 4.2.1 on 2023-05-26 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0002_alcohol_alcoholtype_comment_userprofile_wine_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wine',
        ),
    ]
