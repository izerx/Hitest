# Generated by Django 3.0.4 on 2022-02-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20220215_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='wrong_answers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
