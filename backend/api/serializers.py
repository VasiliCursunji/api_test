from rest_framework import serializers
from .models import Product, ProductImage

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image'
        )

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'sku',
            'price',
            'description'
        )


class ProductDetailViewSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'description',
            'date_post',
            'image',
            'images'
        )


class ProductPaginationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'image'
        )
