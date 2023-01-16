from rest_framework import serializers

from .models import  Orders

class SerializerOrder(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id','firstname','secondname','patronymic','address','type')
