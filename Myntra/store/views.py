from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class ProductView(APIView):
    def get(self,request):
        prod=Product.objects.all()
        dser=ProductModelSerializer(prod,many=True)
        return Response(data=dser.data)
    def post(self,request,):
        ser=ProductModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"ok"})
        return Response(data=ser.errors)          # to show validation errors
    

class SpecificProductView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        prod=Product.objects.get(id=id)
        dser=ProductModelSerializer(prod)
        return Response(data=dser.data)
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        prod=Product.objects.get(id=id)
        prod.delete()
        return Response({"msg":"deleted"})
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        prod=Product.objects.get(id=id)
        ser=ProductModelSerializer(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        return Response(data=ser.errors)


class ProductVSet(ViewSet):
    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        prod=Product.objects.get(id=id)
        dser=ProductModelSerializer(prod)
        return Response(data=dser.data)
    def list(self,request):
        prod=Product.objects.all()
        dser=ProductModelSerializer(prod,many=True)
        return Response(data=dser.data)
    def create(self,request):
        ser=ProductModelSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def update(self,request,*args,**kwargs):
        id = kwargs.get('id')
        prod=Product.objects.get('id')
        ser=ProductModelSerializer(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('id')
        prod=Product.objects.get(id=id)
        prod.delete()
        return Response({'msg':'DELETED'})
    
    @action(methods=['GET'],detail=False)
    def category(self,request,*args,**kwargs):
        cat=Product.objects.values_list('category',flat=True).distinct()
        return Response(data=cat)
    

class ProductMVSet(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Product.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]


class UserVSet(ViewSet):
    def create(self,request):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Created"})
        return Response({"msg":"Failed"})