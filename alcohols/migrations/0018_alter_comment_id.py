# Generated by Django 4.2.1 on 2023-06-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0017_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
