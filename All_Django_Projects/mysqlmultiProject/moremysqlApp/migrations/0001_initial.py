# Generated by Django 3.2.5 on 2021-08-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('smark', models.FloatField()),
                ('saddr', models.CharField(max_length=40)),
            ],
        ),
    ]
