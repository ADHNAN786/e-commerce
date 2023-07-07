
from django.urls import path
from customer.views import *


urlpatterns = [

    path('reg',RegistrationView.as_view(),name='reg'),
    path('logout',LogOut.as_view(),name='logout'),



]
