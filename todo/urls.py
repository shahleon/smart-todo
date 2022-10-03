from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:list_id>/', views.listitems, name='list_items'),
    path('login',views.login, name='login'),
    path('list_templates', views.list_templates, name='list_templates'),
    path('updateListItem', views.updateListItem, name='updateListItem'),
    path('createNewTodoList', views.createNewTodoList, name='createNewTodoList'),
    path('getListItemByName', views.getListItemByName, name='getListItemByName'),
    path('markListItem', views.markListItem, name='markListItem'),

]
