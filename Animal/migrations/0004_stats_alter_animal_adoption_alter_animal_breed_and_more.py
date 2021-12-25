# Generated by Django 4.0 on 2021-12-23 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0003_animal_adoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.IntegerField(blank=True, default=0)),
                ('deleted', models.IntegerField(blank=True, default=0)),
                ('MonthlyChange', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='Adoption',
            field=models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='No', max_length=30, verbose_name='מוכן לאימוץ'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(blank=True, max_length=30, verbose_name='גזע'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.TextField(blank=True, verbose_name='תיאור'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='Animal', verbose_name='העלאת תמונה'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=100, verbose_name='שם'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=30, verbose_name='מין'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], default='Dog', max_length=30, verbose_name='סוג'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='submission_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='תאריך קליטה'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='submitter',
            field=models.CharField(max_length=100, null=True, verbose_name='הוכנס על ידי'),
        ),
    ]
