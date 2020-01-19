from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from payment_api.serializers import RatesSerializer, ReadingsSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework import status
from django.http import Http404
from rest_framework import generics


class rates(generics.ListCreateAPIView):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer

class singleRate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer



class RatesView(viewsets.ModelViewSet):
    queryset = Rates.allRates.all()
    serializer_class = RatesSerializer

class ReadingView(viewsets.ModelViewSet):
    queryset = Readings.objects.all()
    serializer_class = ReadingsSerializer
