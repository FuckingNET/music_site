# Generated by Django 4.0.2 on 2022-05-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_catalog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
