from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
import json


class CustomManager(models.Manager):
    def getRates(self):
        return self.all()

    def insertRate(self, name, rate, rate_1=None, rate_2=None, rate_3=None, formula=None):
        self.name = name
        self.rate = rate
        self.rate_1 = rate_1
        self.rate_2 = rate_2
        self.rate_3 = rate_3
        self.formula = formula
        self.save()


class Rates(models.Model):
    rate_id = models.AutoField(primary_key=True, verbose_name=u"Ідентифікатор")
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Назва")
    rate = models.FloatField(max_length=30, verbose_name=u"Базовий тариф")
    rate_1 = models.FloatField(max_length=30, null=True, verbose_name = u"Перше перевищення")
    rate_2 = models.FloatField(max_length=30, null=True, verbose_name = u"Друге перевищення")
    rate_3 = models.FloatField(max_length=30, null=True, verbose_name = u"Третє перевищення")
    formula = models.CharField(max_length= 300, null=True, verbose_name = u"Формула розрахунку")
    active = models.BooleanField(default=True, verbose_name=u"Активність")

    objects = models.Manager()
    custom = CustomManager()

    def __str__(self):
        return self.name




class Readings(models.Model):
    class Meta:
        unique_together = (('rate_id', 'date_stamp'))

    rate_id = models.ForeignKey('Rates', on_delete=models.CASCADE, verbose_name='Ідентифікатор')
    value = models.FloatField(max_length=30, verbose_name='Показання')
    date_stamp = models.CharField(max_length=30, default=timezone.datetime.now().strftime ("%Y.%m"), verbose_name='Дата внесення')

    def _str__(self):
        return self.name

class Reports(models.Model):
    report_date = models.DateField(default=timezone.now(), verbose_name='Дата створення')
    body = models.TextField(max_length='1000', verbose_name='Звіт')


