from django.urls import path
from .views import *

urlpatterns=[
    path('home',UserHome.as_view(),name='home'),
    path('prodetails/<int:pid>',ProductDetailsView.as_view(),name='prdt'),
    path('cartitmes',CartListView.as_view(),name='vcart'),
    path('cart/<int:pid>',cart,name='cart'),       
    path('deleteitem/<int:pid>',deletecart,name='dcart'),
    path('checkout/<int:cid>',Checkout.as_view(),name='checkout'),
    path('ordercancel/<int:id>',cancel_order,name='cancel'),
    path('orderitem>',Orderitem.as_view(),name='Order'),

]


