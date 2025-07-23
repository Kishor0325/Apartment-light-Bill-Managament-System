from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('create/', views.bill_create, name='bill_create'),
    path('update/<int:pk>/', views.bill_update, name='bill_update'),
    path('delete/<int:pk>/', views.bill_delete, name='bill_delete'),
]
