# Generated by Django 2.0.13 on 2019-04-09 08:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190409_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 8, 31, 30, 275193, tzinfo=utc)),
        ),
    ]