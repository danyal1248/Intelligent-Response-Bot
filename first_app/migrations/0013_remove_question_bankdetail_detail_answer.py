# Generated by Django 2.2.1 on 2019-11-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_auto_20191103_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_bankdetail',
            name='detail_answer',
        ),
    ]
