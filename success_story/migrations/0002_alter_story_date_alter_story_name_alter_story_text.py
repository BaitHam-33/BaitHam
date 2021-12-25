# Generated by Django 4.0 on 2021-12-23 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success_story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='תאריך'),
        ),
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(max_length=100, verbose_name='שם'),
        ),
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.TextField(blank=True, verbose_name='תיאור'),
        ),
    ]
