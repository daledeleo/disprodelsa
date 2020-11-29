from rest_framework import routers
from django.urls import path, include
from .viewsets import ProductoViewSet

router=routers.SimpleRouter()
router.register('productos',ProductoViewSet)

urlpatterns=[
    path('',include(router.urls)),
    ]