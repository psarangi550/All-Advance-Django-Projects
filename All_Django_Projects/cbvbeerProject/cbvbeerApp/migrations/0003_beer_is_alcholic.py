# Generated by Django 3.2.5 on 2021-09-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvbeerApp', '0002_beer_manufacture'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='is_alcholic',
            field=models.BooleanField(default=False),
        ),
    ]
