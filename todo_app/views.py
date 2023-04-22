from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import TodoList, TodoItem
from .forms import RegisterForm, TodoListForm, TodoItemForm
from django.shortcuts import render
import datetime
from django.shortcuts import get_object_or_404


def login_view(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    todo_items = TodoItem.objects.filter(list__user=request.user, due_date__date=datetime.date.today())
    return render(request, 'dashboard.html', {'todo_items': todo_items})

@login_required
def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            return redirect('dashboard')
    else:
        form = TodoListForm()
    return render(request, 'create_todo_list.html', {'form': form})

@login_required
def delete_todo_list(request, list_id):
    todo_list = TodoList.objects.get(pk=list_id, user=request.user)
    todo_list.delete()
    return redirect('dashboard')

@login_required
def create_todo_item(request, list_id):
    todo_list = TodoList.objects.get(pk=list_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            TodoItem.objects.create(todo_list=todo_list, content=content)
            return redirect('dashboard')

    return render(request, 'create_todo_item.html', {'todo_list': todo_list})

@login_required
def edit_todo_item(request, item_id):
    todo_item = TodoItem.objects.get(pk=item_id, list__user=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TodoItemForm(instance=todo_item)
        return render(request, 'edit_todo_item.html', {'form': form})


def view_todo_items(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, pk=todo_list_id)
    todo_items = TodoItem.objects.filter(todo_list=todo_list)
    return render(request, 'view_todo_items.html', {'todo_list': todo_list, 'todo_items': todo_items})


def edit_todo_item(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('view_todo_items', todo_list_id=todo_item.todo_list.id)
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'edit_todo_item.html', {'form': form, 'todo_item': todo_item})

def toggle_completed(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    todo_item.completed = not todo_item.completed
    todo_item.save()
    return redirect('view_todo_items', todo_list_id=todo_item.todo_list.id)

def delete_todo_item(request, todo_item_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_item_id)
    todo_list_id = todo_item.todo_list.id
    todo_item.delete()
    return redirect('view_todo_items', todo_list_id=todo_list_id)
@login_required
def dashboard(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            return redirect('dashboard')
    else:
        form = TodoListForm()

    todo_lists = TodoList.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'form': form, 'todo_lists': todo_lists})
