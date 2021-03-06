# Generated by Django 2.0.13 on 2019-04-24 03:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0061_auto_20190422_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='category',
            field=models.CharField(choices=[('nature', 'Nature'), ('animals', 'Animals'), ('cars', 'Cars'), ('cities', 'Cities'), ('fitness', 'Fitness'), ('motorcycle', 'Motorcycle'), ('people', 'People'), ('space', 'Space'), ('technology', 'Technology')], default='nature', max_length=10),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 3, 20, 8, 984981, tzinfo=utc)),
        ),
    ]
