from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Rates

class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ('rate_id', 'name',  'rate', 'rate_1', 'rate_2', 'rate_3', 'formula', 'active')


