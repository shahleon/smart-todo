from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.index, name='index'),
    path('login', views.login, name='login'),
    path('todo/<int:list_id>', views.index, name='index'),
    path('todo/new-from-template', views.todo_from_template, name='todo_from_template'),
    path('templates', views.template, name='template'),
    path('templates/<int:template_id>', views.template, name='template'),
    path('templates/new-from-todo', views.template_from_todo, name='template_from_todo'),
    path('updateListItem', views.updateListItem, name='updateListItem'),
    path('removeListItem', views.removeListItem, name='removeListItem'),
    path('createNewTodoList', views.createNewTodoList, name='createNewTodoList'),
    path('getListItemByName', views.getListItemByName, name='getListItemByName'),
    path('getListItemById', views.getListItemById, name='getListItemById'),
    path('markListItem', views.markListItem, name='markListItem'),
    path('addNewListItem', views.addNewListItem, name='addNewListItem'),
    path('updateListItem/<int:item_id>', views.updateListItem, name='updateListItem'),
]
