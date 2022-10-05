from django.urls import reverse
from django.test import Client
from django.test import TestCase
from django.utils import timezone


class TodoListTestCase(TestCase):
    def testSavingTodoList(self):
        response = self.client.get(reverse('createNewTodoList'))
        self.assertEqual(response.status_code, 200)
        print(response)