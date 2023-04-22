from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lists = models.ManyToManyField(TodoList)
