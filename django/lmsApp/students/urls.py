from django.urls import path
from .views import *

urlpatterns = [
    path('',all_students,name='students')
]


