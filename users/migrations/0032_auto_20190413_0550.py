# Generated by Django 2.0.13 on 2019-04-13 05:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20190413_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 5, 50, 15, 721956, tzinfo=utc)),
        ),
    ]