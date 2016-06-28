from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # we create an HttpRequest object, which is what django will see when a user's browser asks for a page.
        request = HttpRequest()

        # we pass it to out home_page view, which gives us a response
        # then we insert .content of the response, which is the HTML that we send to the user.
        response = home_page(request)

        # response.content is raw bytes, not a python string, so use b'' syntax to compare them.
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
