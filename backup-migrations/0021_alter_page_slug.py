# Generated by Django 5.0.7 on 2024-08-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devchris', '0020_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]