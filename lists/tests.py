from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

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

        # testing if we're rendering the right template
        expected_html = render_to_string('home.html')

        """
        use decode() to convert the response.content bytes into a
        python unicode string, which allows us to compare strings with strings

        """
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        # expected_html = render_to_string(
        #     'home.html',
        #     {'new_item_text': 'A new list item'}
        # )
        # self.assertEqual(response.content.decode(), expected_html)
