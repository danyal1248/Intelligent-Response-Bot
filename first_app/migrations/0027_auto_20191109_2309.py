# Generated by Django 2.2.1 on 2019-11-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0026_auto_20191109_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newtable',
            name='name',
        ),
        migrations.AddField(
            model_name='newtable',
            name='Code_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newtable',
            name='angry',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='disgust',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='fear',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='happy',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='neutral',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='sad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='surprise',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='newtable',
            name='user_id',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
