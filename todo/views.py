from django.shortcuts import render
from django.http import Http404
from todo.models import List
from todo.models import Template


def index(request):
    latest_lists = List.objects.order_by('-updated_on')[:5]
    saved_templates = Template.objects.order_by('created_on')
    context = {
        'latest_lists': latest_lists,
        'templates': saved_templates
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


def template(request, template_id):
    try:
        fetched_template = Template.objects.get(pk=template_id)
    except Template.DoesNotExist:
        raise Http404("Template does not exist")
    return render(request, 'todo/template.html', {'template': fetched_template})
