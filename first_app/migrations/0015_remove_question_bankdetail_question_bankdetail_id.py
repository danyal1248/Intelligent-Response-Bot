# Generated by Django 2.2.1 on 2019-11-03 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_auto_20191103_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_bankdetail',
            name='Question_BankDetail_id',
        ),
    ]
