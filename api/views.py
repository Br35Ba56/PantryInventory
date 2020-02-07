from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . models import Item
from . serializers import ItemSerializer
# Create your views here.

class ItemList(APIView):

    def get(self, request):
        if request.GET.get('name'):
           items = Item.objects.filter(name=request.GET.get('name'))
        else:
            items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


    def post(self, request):
        if len(request.data['name']) > 0 :
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error' : 'Name cannot be empty'})

class ItemQuantity(APIView):
    
    def get(self, request):
        if request.GET.get('name'):
           items = Item.objects.filter(name=request.GET.get('name'))
           return Response({'quantity': len(items)})
        else:
            items = Item.objects.all()
            return Response({'quantity': len(items)})
    