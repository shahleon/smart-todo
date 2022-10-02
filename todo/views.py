from django.shortcuts import render
from django.http import Http404
from todo.models import List
from todo.models import UserTodoTemplate


def index(request):
    latest_lists = List.objects.order_by('-updated_on')[:5]
    context = {
        'latest_lists': latest_lists,
    }
    return render(request, 'todo/index.html', context)


def listitems(request, list_id):
    try:
        todo_list = List.objects.get(pk=list_id)
    except List.DoesNotExist:
        raise Http404("List does not exist")
    return render(request, 'todo/list_items.html', {'list': todo_list})


def login(request):
    return render(request, 'todo/login.html')


def list_templates(request):
    try:
        templates = UserTodoTemplate.objects.order_by('-updated_on')[:5]
    except UserTodoTemplate.DoesNotExist:
        raise Http404("Templates do not exist")
    return render(request, 'todo/list_templates.html', {'templates': templates})
