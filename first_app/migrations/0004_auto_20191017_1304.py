# Generated by Django 2.2.1 on 2019-10-17 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_job_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_management',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='first_app.UserProfileInfo'),
        ),
    ]
