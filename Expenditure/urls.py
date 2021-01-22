from django.urls import path
from . import views

urlpatterns=[
    path('spend/',views.spend,name="spend"),
]