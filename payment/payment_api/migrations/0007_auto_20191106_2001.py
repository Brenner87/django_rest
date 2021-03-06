# Generated by Django 2.2.6 on 2019-11-06 20:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0006_auto_20191106_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='active',
            field=models.DateField(default=datetime.datetime(2019, 11, 6, 20, 1, 7, 493309, tzinfo=utc), verbose_name='Активовано'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='report_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 6, 20, 1, 7, 494268, tzinfo=utc), verbose_name='Дата створення'),
        ),
    ]
