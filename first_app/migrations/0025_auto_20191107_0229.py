# Generated by Django 2.2.1 on 2019-11-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0024_auto_20191107_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_detail_answer',
            name='Negative_Emotions',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question_detail_answer',
            name='Neutral_Emotions',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question_detail_answer',
            name='positive_Emotions',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
