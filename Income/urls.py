from django.urls import path 
from . import views

urlpatterns=[
    path('choice/',views.choice,name="choice"),
    path('income/',views.income,name="income"),
    path('profit/',views.profit,name="profit"),
    path('info/',views.info,name="info"),
    path('compute/',views.calculate,name="calculate"),
]