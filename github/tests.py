from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from github.views import *
from github.models import Hiren
import os


class HomePageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Hiren: The Bunny</title>', response.content)
        self.assertIn(
            b'<a href="/login"><i class="fa fa-sign-in"></i> Login</a>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


class HirenPageTest(TestCase):

    def setUp(self):
        User.objects.create_superuser(
            username='admin', password='admin', email='admin@admin.lol')

    def tearDown(self):
        pass

    def test_url_resolved_to_hiren_page_view(self):
        found = resolve('/hiren/')
        self.assertEqual(found.func, hiren)



# class LoginFunctionalTestCase(LiveServerTestCase):
#
#     def setUp(self):
#         User.objects.create_superuser(
#             username='admin', password='admin', email='admin@admin.lol')
#         if 'TRAVIS' in os.environ:
#             username = os.environ["SAUCE_USERNAME"]
#             access_key = os.environ["SAUCE_ACCESS_KEY"]
#             hub_url = "%s:%s@ondemand.saucelabs.com:80" % (username, access_key)
#             capabilities = DesiredCapabilities.FIREFOX.copy()
#             # capabilities = {'browserName': "chrome"}
#             capabilities['platform'] = "Linux"
#             capabilities['version'] = "beta"
#             capabilities['screenResolution'] = "1024x768"
#             self.browser = webdriver.Remote(desired_capabilities=capabilities,
#                                             command_executor="http://%s/wd/hub" % hub_url)
#             self.browser.maximize_window()
#             self.browser.implicitly_wait(20)
#         else:
#             self.browser = webdriver.Firefox()
#             self.browser.maximize_window()
#             self.browser.implicitly_wait(5)
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_login_user(self):
#         self.browser.get('%s%s' % (self.live_server_url, "/login/"))
#         import time
#         time.sleep(20)
#         username = self.browser.find_element_by_id("username")
#         username.send_keys('admin')
#         password = self.browser.find_element_by_id("password")
#         password.send_keys('admin')
#         self.browser.find_element_by_id("login").submit()
#         self.assertEqual(self.browser.current_url, '%s%s' % (self.live_server_url, '/hiren/'))


class HirenModelTest(TestCase):

    def test_saving_and_retrieving_item(self):
        item = Hiren()
        item.access_token = "bla bla"
        item.authorized = True
        item.save()

        saved_item = Hiren.objects.all()
        self.assertEqual(saved_item.count(), 1)

        saved_item_content = saved_item[0]
        self.assertEqual(saved_item_content.access_token, "bla bla")
        self.assertEqual(saved_item_content.authorized, True)
