# Generated by Django 4.0 on 2022-01-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_discussion_discuss_alter_discussion_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='email',
            field=models.EmailField(max_length=200, null=True, verbose_name='אימייל'),
        ),
    ]
