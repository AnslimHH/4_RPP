from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from sklad.serializers import SerializerOrder
from .models import Orders

# Create your views here.
class OrdersViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = SerializerOrder



