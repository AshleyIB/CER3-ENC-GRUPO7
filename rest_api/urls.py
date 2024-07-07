from django.urls import path
from . import views

urlpatterns = [
    path('produccion/', views.ProduccionList.as_view(), name='produccion-list'),
    path('produccion/<int:pk>/', views.ProduccionDetail.as_view(), name='produccion-detail'),
]