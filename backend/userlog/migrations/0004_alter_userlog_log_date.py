# Generated by Django 3.2.5 on 2021-11-16 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0003_alter_userlog_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 20, 16, 58, 369790)),
        ),
    ]
