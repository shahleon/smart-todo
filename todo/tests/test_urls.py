from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import index,listitems,todo_from_template,template_from_todo, login,template

class TestURLS(SimpleTestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
