# Generated by Django 3.1.6 on 2021-08-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eno', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
