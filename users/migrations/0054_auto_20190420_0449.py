# Generated by Django 2.0.13 on 2019-04-20 04:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0053_auto_20190420_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 4, 49, 22, 851417, tzinfo=utc)),
        ),
    ]
