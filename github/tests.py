from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from github.views import *
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


class LoginFunctionalTest(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser(
            username='admin', password='admin', email='admin@admin.lol')
        if 'TRAVIS' in os.environ:
            username = os.environ["SAUCE_USERNAME"]
            access_key = os.environ["SAUCE_ACCESS_KEY"]
            hub_url = "%s:%s@localhost:4445" % (username, access_key)
            capabilities = DesiredCapabilities.FIREFOX.copy()
            capabilities['platform'] = "WINDOWS"
            capabilities['version'] = "10"
            browser = webdriver.Remote(desired_capabilities=capabilities,
                command_executor="http://%s/wd/hub" % hub_url)
        else:
            self.browser = webdriver.Firefox()
            self.browser.maximize_window()
            self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_login_user(self):
        self.browser.get('%s%s' % (self.live_server_url,"/login/"))
