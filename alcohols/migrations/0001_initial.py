# Generated by Django 4.2.1 on 2023-05-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('volt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vodka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('volt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('dryness', models.IntegerField()),
                ('votes', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=64)),
                ('volt', models.IntegerField()),
            ],
        ),
    ]
