import datetime
import json

from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError

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


def updateListItem(request):
    if request.method == 'POST':
        post_id = request.GET['post_id']
        # post_request = HttpRequest.POST.get()
        # m = Like(post=likedpost) # Creating Like Object
        # m.save()  # saving it to store in database
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a Post")


def addNewListItem(request):
    if request.method == 'POST':
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a Post")


def markListItem(request):
    if request.method == 'POST':
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
        list_item_name = list_item_name[1:len(list_item_name) - 1]

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
            # return HttpResponse("Request failed when operating on database")
        # return HttpResponse("Success!")  # Sending an success response
    # else:
        # return HttpResponse("Request method is not a Post")
    latest_lists = List.objects.order_by('-updated_on')[:5]
    context = {
        'latest_lists': latest_lists,
    }
    return render(request, 'todo/index.html', context)
