from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ListProductView.as_view(), name='products'),
    path('product/pg/', ProductListPagination.as_view(), name='products_pg'),
    path('product/create/', CreateProductView.as_view(), name='create'),
    path('product/update/<int:pk>/', UpdateProductView.as_view(), name='update'),
    path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete'),
    path('product/detail/<int:pk>/', DetailProductView.as_view(), name='detail'),
]