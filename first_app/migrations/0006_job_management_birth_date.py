# Generated by Django 2.2.1 on 2019-10-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20191017_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_management',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
