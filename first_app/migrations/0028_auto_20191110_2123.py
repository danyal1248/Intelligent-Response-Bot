# Generated by Django 2.2.1 on 2019-11-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0027_auto_20191109_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_management',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job_management',
            name='experience',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job_management',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='job_management',
            name='job_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job_management',
            name='job_type',
            field=models.CharField(max_length=100),
        ),
    ]
