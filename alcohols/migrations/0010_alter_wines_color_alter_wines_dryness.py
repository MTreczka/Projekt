# Generated by Django 4.2.1 on 2023-05-31 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0009_wines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wines',
            name='color',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='wines',
            name='dryness',
            field=models.CharField(max_length=10),
        ),
    ]
