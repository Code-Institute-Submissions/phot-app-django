# Generated by Django 2.0.13 on 2019-04-12 06:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20190412_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='pictures',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 12, 6, 47, 49, 335801, tzinfo=utc)),
        ),
    ]
