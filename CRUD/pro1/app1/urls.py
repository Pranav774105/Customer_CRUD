from django.urls import path
from .views import *

urlpatterns = [
    path('av/', AddView, name='add_url'),
    path('sv/', ShowView, name='show_url'),
]