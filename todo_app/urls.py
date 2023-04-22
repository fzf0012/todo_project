from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_todo_list/', views.create_todo_list, name='create_todo_list'),
    path('delete_todo_list/<int:list_id>/', views.delete_todo_list, name='delete_todo_list'),
    path('create_todo_item/<int:list_id>/', views.create_todo_item, name='create_todo_item'),
    path('view_todo_items/<int:todo_list_id>/', views.view_todo_items, name='view_todo_items'),
    path('edit_todo_item/<int:todo_item_id>/', views.edit_todo_item, name='edit_todo_item'),
    path('toggle_completed/<int:todo_item_id>/', views.toggle_completed, name='toggle_completed'),
    path('delete_todo_item/<int:todo_item_id>/', views.delete_todo_item, name='delete_todo_item'),

]

