from rest_framework import serializers
from . models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields = ('name', 'quantity')
        fields = '__all__'

