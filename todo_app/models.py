from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, default='Default content')

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lists = models.ManyToManyField(TodoList)
