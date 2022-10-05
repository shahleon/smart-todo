import datetime
import json

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError
from django.utils import timezone

from todo.models import List, ListItem, Template, TemplateItem


def index(request, list_id=0):
    if list_id != 0:
        latest_lists = List.objects.filter(id=list_id)
    else:
        latest_lists = List.objects.order_by('-updated_on')[:5]
    latest_list_items = ListItem.objects.order_by('list_id')
    saved_templates = Template.objects.order_by('created_on')
    context = {
        'latest_lists': latest_lists,
        'latest_list_items': latest_list_items,
        'templates': saved_templates
    }
    return render(request, 'todo/index.html', context)


def listitems(request, list_id):
    # todo_list = get_object_or_404(List, pk=list_id)
    # latest_lists = List.objects.filter(id=list_id)
    # latest_list_items = ListItem.objects.order_by('list_id')
    # saved_templates = Template.objects.order_by('created_on')
    # context = {
    #     'latest_lists': latest_lists,
    #     'latest_list_items': latest_list_items,
    #     'templates': saved_templates
    # }
    return redirect('index', list_id)


def login(request):
    return render(request, 'todo/login.html')


def todo_from_template(request):
    template_id = request.POST['template']
    fetched_template = get_object_or_404(Template, pk=template_id)
    todo = List.objects.create(
        title_text=fetched_template.title_text,
        created_on=timezone.now(),
        updated_on=timezone.now()
        # user_id=1 // TODO: assign this to a user
    )
    for template_item in fetched_template.templateitem_set.all():
        ListItem.objects.create(
            item_name=template_item.item_text,
            item_text="",
            created_on=timezone.now(),
            list=todo,
            is_done=False,
        )
    return redirect("/todo")


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
            item_text=todo_item.item_name,
            created_on=timezone.now(),
            template=new_template
        )
    return redirect("/templates")


def template(request, template_id=0):
    if template_id != 0:
        saved_templates = Template.objects.filter(id=template_id)
    else:
        saved_templates = Template.objects.order_by('created_on')
    context = {
        'templates': saved_templates
    }
    return render(request, 'todo/template.html', context)


@csrf_exempt
def removeListItem(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        list_item_id = body['list_item_id']
        print("list_item_id: ", list_item_id)
        try:
            with transaction.atomic():
                being_removed_item = ListItem.objects.get(id=list_item_id)
                being_removed_item.delete()
        except IntegrityError as e:
            print(str(e))
            print("unknown error occurs when trying to update todo list item text")
        return redirect("index")
    else:
        return redirect("index")


@csrf_exempt
def updateListItem(request, item_id):
    if request.method == 'POST':
        updated_text = request.POST['note']
        # print(request.POST)
        print(updated_text)
        print(item_id)
        if item_id <= 0:
            return redirect("index")
        # form = UpdateItemTextForm(request.POST)
        # if form.is_valid():
        #     print("form valid")
        # post_request = HttpRequest.POST.get()
        # m = Like(post=likedpost) # Creating Like Object
        # m.save()  # saving it to store in database
        try:
            with transaction.atomic():
                todo_list_item = ListItem.objects.get(id=item_id)
                todo_list_item.item_text = updated_text
                todo_list_item.save(force_update=True)
        except IntegrityError as e:
            print(str(e))
            print("unknown error occurs when trying to update todo list item text")
        return redirect("index")
    else:
        return redirect("index")


@csrf_exempt
def addNewListItem(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        list_id = body['list_id']
        item_name = body['list_item_name']
        create_on = body['create_on']
        create_on_time = datetime.datetime.fromtimestamp(create_on)
        print(item_name)
        print(create_on)
        result_item_id = -1
        # create a new to-do list object and save it to the database
        try:
            with transaction.atomic():
                todo_list_item = ListItem(item_name=item_name, created_on=create_on_time, list_id=list_id, item_text="", is_done=False)
                todo_list_item.save()
                result_item_id = todo_list_item.id
        except IntegrityError:
            print("unknown error occurs when trying to create and save a new todo list")
            return JsonResponse({'item_id': -1})
        return JsonResponse({'item_id': result_item_id})  # Sending an success response
    else:
        return JsonResponse({'item_id': -1})


@csrf_exempt
def markListItem(request):
    """
    Mark a list item as done or undo it
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        list_id = body['list_id']
        list_item_name = body['list_item_name']
        list_item_id = body['list_item_id']
        # remove the first " and last "
        list_item_is_done = True
        is_done_str = str(body['is_done'])
        print("is_done: " + str(body['is_done']))
        if is_done_str == "0" or is_done_str == "False" or is_done_str == "false":
            list_item_is_done = False
        try:
            with transaction.atomic():
                query_list = List.objects.get(id=list_id)
                query_item = ListItem.objects.get(id=list_item_id)
                query_item.is_done = list_item_is_done
                query_item.save()
                # Sending an success response
                return JsonResponse({'item_name': query_item.item_name, 'list_name': query_list.title_text, 'item_text': query_item.item_text})
        except IntegrityError:
            print("query list item" + str(list_item_name) + " failed!")
            JsonResponse({})
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a Post")

@csrf_exempt
def getListItemByName(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        list_id = body['list_id']
        list_item_name = body['list_item_name']
        # remove the first " and last "
        # list_item_name = list_item_name

        print("list_id: " + list_id)
        print("list_item_name: " + list_item_name)
        try:
            with transaction.atomic():
                query_list = List.objects.get(id=list_id)
                query_item = ListItem.objects.get(list_id=list_id, item_name=list_item_name)
                # Sending an success response
                return JsonResponse({'item_id': query_item.id, 'item_name': query_item.item_name, 'list_name': query_list.title_text, 'item_text': query_item.item_text})
        except IntegrityError:
            print("query list item" + str(list_item_name) + " failed!")
            JsonResponse({})
    else:
        return JsonResponse({'result': 'get'})  # Sending an success response


@csrf_exempt
def getListItemById(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        list_id = body['list_id']
        list_item_name = body['list_item_name']
        list_item_id = body['list_item_id']
        # remove the first " and last "
        # list_item_name = list_item_name

        print("list_id: " + list_id)
        print("list_item_name: " + list_item_name)
        print("list_item_id: " + list_item_id)
        try:
            with transaction.atomic():
                query_list = List.objects.get(id=list_id)
                query_item = ListItem.objects.get(id=list_item_id)
                print("item_text", query_item.item_text)
                # Sending an success response
                return JsonResponse({'item_id': query_item.id, 'item_name': query_item.item_name, 'list_name': query_list.title_text, 'item_text': query_item.item_text})
        except IntegrityError:
            print("query list item" + str(list_item_name) + " failed!")
            JsonResponse({})
    else:
        return JsonResponse({'result': 'get'})  # Sending an success response


@csrf_exempt
def createNewTodoList(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        list_name = body['list_name']
        create_on = body['create_on']
        create_on_time = datetime.datetime.fromtimestamp(create_on)
        print(list_name)
        print(create_on)
        # create a new to-do list object and save it to the database
        try:
            with transaction.atomic():
                todo_list = List(title_text=list_name, created_on=create_on_time, updated_on=create_on_time)
                todo_list.save()
        except IntegrityError:
            print("unknown error occurs when trying to create and save a new todo list")
            return HttpResponse("Request failed when operating on database")
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a Post")
    # latest_lists = List.objects.order_by('-updated_on')[:5]
    # context = {
    #     'latest_lists': latest_lists,
    # }
    # return render(request, 'todo/index.html', context)
