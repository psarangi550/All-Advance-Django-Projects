# Generated by Django 3.2.5 on 2021-11-22 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelformsetapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='loc',
        ),
    ]