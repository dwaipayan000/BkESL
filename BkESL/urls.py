from django.urls import path
from django.conf.urls import url, include
# importing views from views..py
from . import views

urlpatterns = [

    path('', views.HomePageView.as_view(), name='login'),

    path('search/', views.search, name='search'),

    path('homepage/', views.search, name='homepage'),

    path('consumption/', views.consumption, name='consumption'),

    path('consumptionD1/', views.consumption_d1, name='consumptionD1'),

    path('consumptionD2/', views.consumption_d2, name='consumptionD2'),

    path('consumptionD3/', views.consumption_d3, name='consumptionD3'),

    path('consumptionD4/', views.consumption_d4, name='consumptionD4'),

    path('consumptionD5/', views.consumption_d5, name='consumptionD5'),

    path('consumptionD6/', views.consumption_d6, name='consumptionD6'),

    path('consumptionD7/', views.consumption_d7, name='consumptionD7'),

    path('consumptionD8/', views.consumption_d8, name='consumptionD8'),

    path('sale/', views.sale, name='sale'),

    path('EHT/', views.EHT, name='EHT'),

    path('loss/', views.loss, name='loss'),

    path('Vigilance/', views.Vigilance, name='vigilance'),

    path('cumulative/', views.cumulative, name='cumulative'),

    path('comparison/', views.comparison, name='comparison'),

]
