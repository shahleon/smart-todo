from django.test import TestCase, Client
from django.urls import reverse

from todo.models import List
import json


class TestViews(TestCase):

    def test_template_from_todo(self):
        client = Client()
        test_list = List()
        response = client.get(reverse('todo:template_from_todo'))
        self.assertEquals(response.status_code, 200)