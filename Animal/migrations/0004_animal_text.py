# Generated by Django 3.2.9 on 2021-11-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0003_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]