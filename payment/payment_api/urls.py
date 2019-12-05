from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
#from payment_api import views
from . import views


router = routers.DefaultRouter()
router.register('rates', views.RatesView)





urlpatterns = [
    #path('rates/get/', views.get_rates, name='get_rates'),
    #path('rates/get/', views.Rates, name='get_rates'),
    #path('rates/post/', views.insert_rates, name='insert_rates')
    path('', include(router.urls)),
]
