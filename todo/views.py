from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from todo.models import List, ListItem, Template, TemplateItem
from django.utils import timezone


def index(request):
    latest_lists = List.objects.order_by('-updated_on')[:5]
    saved_templates = Template.objects.order_by('created_on')
    context = {
        'latest_lists': latest_lists,
        'templates': saved_templates
    }
    return render(request, 'todo/index.html', context)


def listitems(request, list_id):
    todo_list = get_list_or_404(List, pk=list_id)
    return render(request, 'todo/list_items.html', {'list': todo_list})


def todo_from_template(request):
    template_id = request.POST['template']
    fetched_template = get_object_or_404(Template, pk=template_id)
    todo = List.objects.create(
        title_text=fetched_template.title_text,
        created_on=timezone.now(),
        updated_on=timezone.now()
        # user_id=1 // TODO: assign this to a user
    )
    return HttpResponseRedirect(str(todo.id))


def template_from_todo(request):
    todo_id = request.POST['todo']
    fetched_todo = get_object_or_404(List, pk=todo_id)
    new_template = Template.objects.create(
        title_text=fetched_todo.title_text,
        created_on=timezone.now(),
        updated_on=timezone.now()
    )
    for todo_item in fetched_todo.listitem_set.all():
        TemplateItem.objects.create(
            item_text=todo_item.item_text,
            created_on=timezone.now(),
            template=new_template
        )
    return HttpResponseRedirect("/templates/" + str(new_template.id))


def login(request):
    return render(request, 'todo/login.html')


def template(request, template_id):
    latest_lists = List.objects.order_by('-updated_on')[:5]
    saved_templates = Template.objects.order_by('created_on')
    fetched_template = get_object_or_404(Template, pk=template_id)
    context = {
        'latest_lists': latest_lists,
        'templates': saved_templates,
        'template': fetched_template
    }
    return render(request, 'todo/template.html', context)
