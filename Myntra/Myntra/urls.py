"""
URL configuration for Myntra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from customer.views import LoginPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.url')),
    path('',LoginPage.as_view(),name='login'),
    path('user/',include('user.urls')),
    path('store/',include('store.urls'))

    # path('reg',RegistraionView.as_view(),name='reg'),
    # path('',LoginPage.as_view(),name='login'),
    # path('home',HomePage.as_view(),name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
