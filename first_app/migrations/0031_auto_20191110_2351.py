# Generated by Django 2.2.1 on 2019-11-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0030_auto_20191110_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_bank',
            name='id',
        ),
        migrations.AddField(
            model_name='question_bank',
            name='detail_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
