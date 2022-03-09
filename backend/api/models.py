from django.db import models


def upload_path(self, filename):
    return '/'.join(['images', self.product.name, filename])


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    description = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=upload_path)

    def __str__(self):
        return self.product.name
