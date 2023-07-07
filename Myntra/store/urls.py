from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('prod',ProductVSet,basename='prod')
router.register('prodmvt',ProductMVSet,basename='prodmvt')
router.register('user',UserVSet,basename='us')
# localhost:8000/store/prod/

urlpatterns = [
    path('product',ProductView.as_view()),
    path('product/<int:id>',SpecificProductView.as_view()),
    path('token',views.obtain_auth_token),



]+router.urls
