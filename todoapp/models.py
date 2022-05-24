from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Todo(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    todo = models.ForeignKey(Todo, on_delete=CASCADE)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.description

