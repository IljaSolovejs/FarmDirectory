from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm_list, name='farm_list'),
    path('<int:farm_id>/', views.farm_detail, name='farm_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('request-info/', views.request_info, name='request_info'),
    path('references/', views.references, name='references'),
    path('about/', views.about, name='about'),
]