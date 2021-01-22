from django.urls import path
from . import views

urlpatterns =[
    path('',views.base,name="base"),

    path('team/',views.team,name="team"),
    path('about/',views.about,name="about"),
]