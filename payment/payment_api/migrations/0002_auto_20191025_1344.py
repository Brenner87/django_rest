# Generated by Django 2.2.6 on 2019-10-25 13:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readings',
            name='date_stamp',
            field=models.DateField(default=datetime.datetime(2019, 10, 25, 13, 44, 47, 171237, tzinfo=utc), verbose_name='Дата внесення'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='report_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 25, 13, 44, 47, 171588, tzinfo=utc), verbose_name='Дата створення'),
        ),
    ]
