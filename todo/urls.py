from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<int:list_id>', views.listitems, name='list_items'),
    path('login', views.login, name='login'),
    path('templates/<int:template_id>', views.template, name='template'),
    path('todo/new-from-template', views.todo_from_template, name='todo_from_template')
]
