# Generated by Django 4.0 on 2021-12-25 00:23

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
                ('genre', models.CharField(choices=[('adoption', 'Adoption'), ('info', 'Info'), ('training', 'Training'), ('other', 'Other')], default='other', max_length=200)),
                ('link', models.CharField(default=None, max_length=2000)),
            ],
        ),
    ]
