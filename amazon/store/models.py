from django.db import models

# Create your models here.

class User(models.Model):
    pass

class Shop(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="shop")

class Product(models.Model):
    shop = models.ForeignKey(Shop, null=True, on_delete=models.CASCADE, related_name="products")

class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="review")

