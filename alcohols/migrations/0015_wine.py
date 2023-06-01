# Generated by Django 4.2.1 on 2023-05-31 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0014_rename_alc_comment_alcohols'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcohol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='alcohols.alcohol')),
                ('dryness', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]