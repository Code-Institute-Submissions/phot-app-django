# Generated by Django 2.0.13 on 2019-04-20 06:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0055_auto_20190420_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 6, 2, 14, 765775, tzinfo=utc)),
        ),
    ]