from selenium import webdriver
from todo.models import User, List, ListItem, Template, TemplateItem
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

class TestProjectListPage(StaticLiveServerTestCase):

    def setUP(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()