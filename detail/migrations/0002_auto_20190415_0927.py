# Generated by Django 2.0.13 on 2019-04-15 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20190415_0927'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Pictures'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
