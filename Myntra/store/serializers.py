from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

    def validate(self, attrs):
        price=attrs.get('price')
        name=attrs.get('price')

        if price<0:
            raise serializers.ValidationError('Invalid Price Amount')
        return attrs
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "username",
            "password",
            "email"
        ]

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)