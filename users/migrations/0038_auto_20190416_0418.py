# Generated by Django 2.0.13 on 2019-04-16 04:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20190415_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 4, 18, 40, 441347, tzinfo=utc)),
        ),
    ]