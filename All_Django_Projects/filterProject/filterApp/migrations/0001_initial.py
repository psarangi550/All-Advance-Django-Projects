# Generated by Django 3.2.5 on 2021-09-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]