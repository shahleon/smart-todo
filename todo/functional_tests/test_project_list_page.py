from selenium import webdriver
from todo.models import User, List, ListItem, Template, TemplateItem
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

# class TestProjectLivePage(StaticLiveServerTestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
#
#     def tearDown(self):
#         self.browser.close()
#
#     def test(self):
#         self.browser.get(self.live_server_url)
#         time.sleep(20)
