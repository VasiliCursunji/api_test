from rest_framework import generics
from .serializers import *
from .models import Product
from .service import PaginationProduct


class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailViewSerializer


class ProductListPagination(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductPaginationViewSerializer
    pagination_class = PaginationProduct
