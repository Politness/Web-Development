from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('cat_item/',cat_item),
    path('cats/', categories),
    
    path('products/', list_products),
    path('products/<int:get_id>/', get_product),
    path('categories/', list_categories),
    path('categories/<int:get_id>/', get_category),
    path('categories/<int:get_id>/products/', product_category),
]
