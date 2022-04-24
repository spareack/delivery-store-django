from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50, default="None")
    food_list = models.TextField(default="[]")
    filename = models.ImageField(default="-1.png")


class Food(models.Model):
    name = models.CharField(max_length=50, default="None")
    price = models.CharField(max_length=10, default="None")
    weight = models.CharField(max_length=10, default="None")
    description = models.TextField(default="None")
    filename = models.TextField(default="-1.png")
