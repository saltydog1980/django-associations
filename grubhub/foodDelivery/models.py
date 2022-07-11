from django.db import models

# Create your models here.

class User(models.Model):
    pass

class Restaurant(models.Model):
    pass

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE, related_name="orders")

class FoodItem(models.Model):
    orders = models.ManyToManyField(Order, through="orderfooditem", related_name="food_items")


class OrderFoodItem(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("order", "food_item")) 
