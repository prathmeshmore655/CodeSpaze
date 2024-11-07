from django.urls import path
from .views import ProductList

urlpatterns = [
    path('productList/', ProductList.as_view(), name='product_list_api'),  # For GET and POST
    path('productList/<int:pk>/', ProductList.as_view(), name='product_list_var_api'),  # For GET, PUT, DELETE
]
