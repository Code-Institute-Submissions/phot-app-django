# Generated by Django 2.0.13 on 2019-04-16 06:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20190416_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 6, 45, 57, 310061, tzinfo=utc)),
        ),
    ]
