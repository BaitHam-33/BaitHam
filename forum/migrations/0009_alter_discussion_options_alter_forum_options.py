# Generated by Django 4.0 on 2022-01-03 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_alter_forum_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discussion',
            options={'verbose_name_plural': 'דיונים'},
        ),
        migrations.AlterModelOptions(
            name='forum',
            options={'verbose_name_plural': 'פורום'},
        ),
    ]
