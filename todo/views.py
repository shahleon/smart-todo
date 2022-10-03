import datetime
import json

from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError

from todo.forms import UpdateItemTextForm
from todo.models import List, ListItem


def index(request):
    latest_lists = List.objects.order_by('-updated_on')[:5]
    latest_list_items = ListItem.objects.order_by('list_id')
    context = {
        'latest_lists': latest_lists,
        'latest_list_items': latest_list_items,
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
    return render(request, 'todo/list_templates.html')


@csrf_exempt
def updateListItem(request):
    if request.method == 'POST':
        form = UpdateItemTextForm(request.POST)
        if form.is_valid():
            print("form valid")
        # post_request = HttpRequest.POST.get()
        # m = Like(post=likedpost) # Creating Like Object
        # m.save()  # saving it to store in database
        return redirect("index")
    else:
        return HttpResponse("Request method is not a Post")


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
                return JsonResponse({'item_name': query_item.item_name, 'list_name': query_list.title_text, 'item_text': query_item.item_text})
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
