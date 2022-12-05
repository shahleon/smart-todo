from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from todo.views import login_request, template_from_todo, template, delete_todo, index
from django.utils import timezone
from todo.models import List, ListItem, Template, TemplateItem


class TestViews(TestCase):
    def setUp(self):
        # Every test needs access to the client and request factory.
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def testLogin(self):
        request = self.factory.get('/login/')
        request.user = self.user
        post = request.POST.copy()  # to make it mutable
        post['todo'] = 1
        print(request)
        request.POST = post
        response = login_request(request)
        self.assertEqual(response.status_code, 200)

    def testSavingTodoList(self):
        response = self.client.get(reverse('todo:createNewTodoList'))
        self.assertEqual(response.status_code, 302)
        # print(response)

    def test_delete_todo_list(self):
        request = self.factory.get('/todo/')
        request.user = self.user
        todo = List.objects.create(
            title_text="test list",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id_id=self.user.id,
        )
        ListItem.objects.create(
            item_name="test item",
            item_text="This is a test item on a test list",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            tag_color="#f9f9f9",
            due_date=timezone.now(),
            list=todo,
            is_done=False,
        )
        post = request.POST.copy()
        post['todo'] = 1
        request.POST = post
        response = delete_todo(request)
        self.assertEqual(response.status_code, 302)

    def test_index(self):
        request = self.factory.get('/todo/')
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_template_from_todo_redirect(self):
        client = self.client
        response = client.get(reverse('todo:template_from_todo'))
        self.assertEquals(response.status_code, 302)

    def test_template_from_todo_function(self):
        request = self.factory.get('/todo/')
        request.user = self.user
        todo = List.objects.create(
            title_text="test list",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id_id=request.user.id,
        )
        item = ListItem.objects.create(
            item_name="test item",
            item_text="This is a test item on a test list",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            tag_color="#f9f9f9",
            due_date=timezone.now(),
            list=todo,
            is_done=False,
        )
        post = request.POST.copy()  # to make it mutable
        post['todo'] = 1
        request.POST = post
        response = template_from_todo(request)
        self.assertEqual(response.status_code, 302)

    def test_template_display(self):
        request = self.factory.get('/todo/')
        request.user = self.user
        new_template = Template.objects.create(
            title_text="test template",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id_id=request.user.id
        )
        template_item = TemplateItem.objects.create(
            item_text="test item",
            created_on=timezone.now(),
            template=new_template,
            finished_on=timezone.now(),
            tag_color="#f9f9f9",
            due_date=timezone.now()
        )
        post = request.POST.copy()  # to make it mutable
        post['todo'] = 1
        request.POST = post
        response = template(request, 1)
        self.assertEqual(response.status_code, 200)
