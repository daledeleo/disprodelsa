from rest_framework import routers
from django.urls import path, include
from .views import *
from django.conf.urls import url,include

router=routers.DefaultRouter()
router.register('email',EmailViewSet)
router.register('usuarios del sitema',UsuarioSistemaViewSet)
router.register(r'login', UserLogin, basename='login')

urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    ]