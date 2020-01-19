# Generated by Django 2.2.6 on 2019-12-30 11:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0010_auto_20191224_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readings',
            name='date_stamp',
            field=models.DateField(default=datetime.date(2019, 12, 1), verbose_name='Дата внесення'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='report_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 30, 11, 48, 22, 934800, tzinfo=utc), verbose_name='Дата створення'),
        ),
    ]
