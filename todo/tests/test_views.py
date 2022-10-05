from django.urls import reverse
from django.utils import timezone
from django.test import TestCase, Client

from todo.models import List
import json


class TodoListTestCase(TestCase):
    def testSavingTodoList(self):
        response = self.client.get(reverse('createNewTodoList'))
        self.assertEqual(response.status_code, 200)
        print(response)


class TestViews(TestCase):

    def test_template_from_todo(self):
        client = Client()
        test_list = List()
        response = client.get(reverse('todo:template_from_todo'))
        self.assertEquals(response.status_code, 200)