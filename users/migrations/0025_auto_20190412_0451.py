# Generated by Django 2.0.13 on 2019-04-12 04:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20190412_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 12, 4, 51, 16, 445144, tzinfo=utc)),
        ),
    ]
