# Generated by Django 2.0.13 on 2019-04-22 06:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0060_auto_20190422_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 6, 15, 10, 793209, tzinfo=utc)),
        ),
    ]
