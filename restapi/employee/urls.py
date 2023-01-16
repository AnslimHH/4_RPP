from django.urls import path

from employee.views import *

urlpatterns = [
    path('', index, name='index')
]