from django.shortcuts import render

from django.http import HttpResponse, HttpResponseForbidden
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
class CreateUser(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error' : 'Could not serialize'}, status=status.HTTP_400_BAD_REQUEST)


class ItemList(APIView):

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def get(self, request):
        user_id = request.user.id
        if request.GET.get('name'):
            items = Item.objects.filter(name__contains=request.GET.get('name'), user_id=user_id)
        else:
            items = Item.objects.filter(user_id=user_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


    def post(self, request):
        if len(request.data['name']) > 0 :
            request.data['user_id'] = request.user.id
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                return Response(ItemSerializer(self.update_or_save(serializer.validated_data)).data)
            else:
                return Response({'error' : 'Could not serialize'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data)
        else:
            return Response({'error' : 'Name cannot be empty'})


    def delete(self, request, id):
        item = get_object_or_404(Item, pk=id)
        if request.user.id == item.user_id.id:
            item.delete()
            return Response({"item deleted": "true", "id" : id})
        else:
            return HttpResponseForbidden({"error": "User does not own this item"})


    def update_or_save(self, validated_data):
        if 'id' in validated_data:
            try:
                item = Item.objects.get(pk=validated_data.get('id'))
                item.delete()
                return Item.objects.create(id=validated_data.get('id'),
                                    name = validated_data.get('name'),
                                    quantity_with_unit = validated_data.get('quantity_with_unit'),
                                    acquisition_date = validated_data.get('acquisition_date'),
                                    expiration_date = validated_data.get('expiration_date'),
                                    user_id = validated_data.get('user_id'))
            except:
                print('no item exists')
        
        else:
            return Item.objects.create(name = validated_data.get('name'),
                                quantity_with_unit = validated_data.get('quantity_with_unit'),
                                acquisition_date = validated_data.get('acquisition_date'),
                                expiration_date = validated_data.get('expiration_date'),
                                user_id = validated_data.get('user_id'))
        return None
        
