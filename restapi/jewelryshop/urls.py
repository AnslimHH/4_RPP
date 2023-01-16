from django.urls import path

from jewelryshop.views import *

urlpatterns = [
    path('', index, name='index')
]