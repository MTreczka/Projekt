# Generated by Django 4.2.1 on 2023-06-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0026_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='color',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='wine',
            name='dryness',
            field=models.CharField(max_length=24),
        ),
    ]