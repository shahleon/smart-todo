from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('todo/<int:list_id>', views.listitems, name='list_items'),
    path('todo/new-from-template', views.todo_from_template, name='todo_from_template'),
    path('templates/<int:template_id>', views.template, name='template'),
    path('templates/new-from-todo', views.template_from_todo, name='template_from_todo'),
]
