# Generated by Django 4.0 on 2021-12-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Taskboard', '0003_list_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
