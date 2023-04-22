from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Add this line
from django import forms

from .models import TodoList, TodoItem

# ...


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name', 'description']

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['name', 'description', 'status', 'due_date']
        widgets = {'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})}