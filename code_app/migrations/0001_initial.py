# Generated by Django 5.0.7 on 2024-08-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('question', models.TextField()),
                ('rating', models.TextField()),
                ('submitted_date', models.DateTimeField()),
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]