# Generated by Django 2.0.13 on 2019-04-22 06:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0058_auto_20190422_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 6, 13, 25, 574845, tzinfo=utc)),
        ),
    ]