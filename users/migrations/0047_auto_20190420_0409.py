# Generated by Django 2.0.13 on 2019-04-20 04:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_auto_20190420_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 4, 9, 23, 414912, tzinfo=utc)),
        ),
    ]