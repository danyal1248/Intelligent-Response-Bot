# Generated by Django 2.2.1 on 2019-11-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0032_auto_20191111_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_management',
            name='id',
        ),
        migrations.AddField(
            model_name='job_management',
            name='detail_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interview_invite',
            name='Interviewr_Experience',
            field=models.CharField(max_length=200),
        ),
    ]
