from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Rates, Readings

class RatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rates
        fields = ('rate_id', 'url', 'name',  'rate', 'rate_1', 'rate_2', 'rate_3', 'formula', 'active')


class ReadingsSerializer(serializers.HyperlinkedModelSerializer):
    #rate_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Rates.activeRates.all())
    class Meta:
        model = Readings
        fields = ('id', 'rate_id', 'url', 'value', 'date_stamp')
        read_only_fields = ('date_stamp',)



