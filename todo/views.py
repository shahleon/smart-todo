from django.shortcuts import render
from django.http import Http404
from todo.models import List
from todo.models import Template


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


def templates(request):
    try:
        saved_templates = Template.objects.order_by('created_on')
    except Template.DoesNotExist:
        raise Http404("Templates do not exist")
    return render(request, 'todo/templates.html', {'templates': saved_templates})
