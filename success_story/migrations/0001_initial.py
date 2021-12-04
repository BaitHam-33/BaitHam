# Generated by Django 3.2.9 on 2021-11-29 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]
