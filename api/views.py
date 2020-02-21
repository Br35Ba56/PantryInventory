from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . models import Item
from . serializers import ItemSerializer
from . serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.

class ItemList(APIView):

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def get(self, request):
        user_id = request.user.id
        
        if request.GET.get('name'):
           items = Item.objects.filter(name=request.GET.get('name'), user_id=user_id)
           print('Quanity ' + str(len(items)))
        else:
            items = Item.objects.filter(user_id=user_id)
            print('Quanity ' + str(len(items)))
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


    def post(self, request):
        if len(request.data['name']) > 0 :
            request.data['user_id'] = request.user.id
            serializer = ItemSerializer(data=request.data)
            
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'error' : 'Could not serialize'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data)
        else:
            return Response({'error' : 'Name cannot be empty'})


    
