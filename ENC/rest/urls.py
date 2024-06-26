from django.urls import path, include
from rest_framework import serializers, routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls))
]