# Generated by Django 2.1.5 on 2022-04-21 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20220421_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 21, 54, 11, 454019)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 21, 54, 11, 454019)),
        ),
    ]