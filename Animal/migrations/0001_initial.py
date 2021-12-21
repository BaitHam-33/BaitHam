# Generated by Django 4.0 on 2021-12-18 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('submitter', models.CharField(max_length=100, null=True)),
                ('species', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], default='Dog', max_length=30)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=30)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='Animal')),
                ('Adoption', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='No', max_length=30)),
            ],
        ),
    ]