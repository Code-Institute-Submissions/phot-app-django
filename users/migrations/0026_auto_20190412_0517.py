# Generated by Django 2.0.13 on 2019-04-12 05:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20190412_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='images',
        ),
        migrations.AddField(
            model_name='pictures',
            name='category',
            field=models.CharField(choices=[('nature', 'Nature'), ('animals', 'Animals'), ('cars', 'Cars'), ('cities', 'Cities'), ('fitness', 'Fitness'), ('motorcycles', 'Motorcycles'), ('people', 'People'), ('space', 'Space'), ('technology', 'Technology')], default='nature', max_length=10),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 12, 5, 17, 4, 369544, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
