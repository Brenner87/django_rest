# Generated by Django 2.2.6 on 2019-11-06 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0005_auto_20191106_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='report_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 6, 19, 53, 10, 854530, tzinfo=utc), verbose_name='Дата створення'),
        ),
    ]
