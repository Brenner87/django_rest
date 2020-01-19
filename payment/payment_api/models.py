from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
import json


class AcitiveRatesManager(models.Manager):
    def get_queryset(self):
        return super(AcitiveRatesManager, self).get_queryset().filter(active=True)

class AllRatesManager(models.Manager):
    def get_queryset(self):
        return super(AllRatesManager, self).get_queryset().all()


class Rates(models.Model):
    rate_id = models.AutoField(primary_key=True, verbose_name=u"Ідентифікатор")
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Назва")
    rate = models.FloatField(max_length=30, verbose_name=u"Базовий тариф")
    rate_1 = models.FloatField(max_length=30, null=True, verbose_name = u"Перше перевищення")
    rate_2 = models.FloatField(max_length=30, null=True, verbose_name = u"Друге перевищення")
    rate_3 = models.FloatField(max_length=30, null=True, verbose_name = u"Третє перевищення")
    formula = models.CharField(max_length= 300, null=True, verbose_name = u"Формула розрахунку")
    active = models.BooleanField(default=True, verbose_name=u"Активність")

    objects = AcitiveRatesManager()
    allRates = AllRatesManager()

    def __str__(self):
        return self.name




class Readings(models.Model):
    class Meta:
        unique_together = (('rate_id', 'date_stamp'))

    rate_id = models.ForeignKey('Rates', on_delete=models.CASCADE, verbose_name='Ідентифікатор')
    value = models.FloatField(max_length=30, verbose_name='Показання')
    date_stamp = models.DateField(default=datetime.date( timezone.now().year,  timezone.now().month, 1),
verbose_name='Дата внесення')

    def _str__(self):
        return '{}_{}'.format(self.rate_id, self.date_stamp)

class Reports(models.Model):
    report_date = models.DateField(default=timezone.now(), verbose_name='Дата створення')
    body = models.TextField(max_length='1000', verbose_name='Звіт')


