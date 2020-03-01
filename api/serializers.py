from rest_framework import serializers
from . models import Item
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    
    class Meta:
        model = Item
        #fields = ('id', 'name', 'quantity_with_unit', 'acquisition_date', 'expiration_date')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)
    def create(self, validated_data):
        print(validated_data['password'])
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        user_group = Group.objects.get(name='api_user_group') 
        user_group.user_set.add(user)
        return user

    class Meta:
        model = User
        fields = ('id', 'username',  'password')