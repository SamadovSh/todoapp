# Generated by Django 2.1.5 on 2022-04-21 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 21, 49, 13, 282968)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 21, 49, 13, 282968)),
        ),
    ]
