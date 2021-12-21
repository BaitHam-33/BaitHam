# Generated by Django 3.2.9 on 2021-11-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=5000)),
                ('type', models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('story', models.TextField(max_length=5000)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]