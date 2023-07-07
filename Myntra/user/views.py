from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView
from store.models import Product
from .models import Cart,Order
from django.contrib import messages
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


#auth_decorator

def sign_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            # messages.error(request,'Please Login First!!')
            return redirect('login')
        
    return inner

dec=[sign_required,never_cache]

# Create your views here.

@method_decorator(dec,name='dispatch')
class UserHome(ListView):
    template_name='home.html'
    model=Product
    context_object_name='data'
    
@method_decorator(dec,name='dispatch')
class ProductDetailsView(DetailView):
    template_name='details.html'
    model=Product
    context_object_name='product'
    pk_url_kwarg='pid'


dec
def cart(request,pid):
    prod=Product.objects.get(id=pid)
    user=request.user
    Cart.objects.create(product=prod,user=user)
    messages.success(request,'Product Added To Cart!!!')
    return redirect('home')


@method_decorator(dec,name='dispatch')
class CartListView(ListView):
    template_name="cart-list.html"
    model = Cart
    context_object_name='cartitem'

    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user,status='cart')
        total=Cart.objects.filter(user=self.request.user,status="cart").aggregate(amount=Sum('product__price'))
        return {'items': cart , 'total':total}

dec   
def deletecart(request,pid):
    item=Cart.objects.get(id=pid)
    item.delete()
    messages.success(request,'Cart Item removed!')
    return redirect('vcart')


@method_decorator(dec,name='dispatch')
class Checkout(View):
    def get(self,request,*args,**kwargs):
        return render(request,'checkout.html')
    def post(self,request,*args,**kwargs):
        id=kwargs.get('cid')
        cart=Cart.objects.get(id=id)
        prod=cart.product
        user=request.user
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        Order.objects.create(product=prod,user=user,address=address,phone=phone)
        cart.status='Order Placed!'
        cart.save()
        messages.success(request,"Order Placed Successfully!!")
        return redirect('home')


@method_decorator(dec,name='dispatch')
class Orderitem(ListView):
    template_name='Orders.html'
    model=Order
    context_object_name='order'

    def get_queryset(self):
        order=Order.objects.filter(user=self.request.user)
        return {'order':order}

dec   
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status= "Cancel"
    order.save()
    messages.success(request,"Order Cancelled")
    return redirect('Order')