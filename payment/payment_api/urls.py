from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
#from payment_api import views
from . import views


router = routers.DefaultRouter()
router.register('rates', views.RatesView)
router.register('readings', views.ReadingView)





urlpatterns = [
    # path('rates/', views.rates.as_view(), name='rates'),
    # path('rates/<int:pk>/', views.singleRate.as_view())
    #path('rates/get/', views.Rates, name='get_rates'),
     path('', include(router.urls)),
    # path('rates_1/', views.viewRates.as_view()),
    # path('rates_1/<int:pk>/', views.SingleRate.as_view()),
]
