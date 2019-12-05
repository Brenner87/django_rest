from django.shortcuts import render
from rest_framework import viewsets
from payment_api.serializers import RatesSerializer
from django.http import HttpResponse
from .models import *
import json

def get_rates(request):
    return HttpResponse(Rates.custom.getRates())


def insert_rates(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        return HttpResponse(json.loads(data))
    return None

class RatesView(viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer