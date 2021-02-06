from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    #image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    messege=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

