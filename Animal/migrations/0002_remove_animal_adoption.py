# Generated by Django 4.0 on 2021-12-18 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='Adoption',
        ),
    ]
