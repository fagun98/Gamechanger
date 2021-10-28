from django.contrib import admin
from django.urls import path

from . import views 

app_name = 'cricket' 
urlpatterns = [
    path('',views.index , name = 'index' ),
    path('formation/', views.formation , name='formation'),
]
