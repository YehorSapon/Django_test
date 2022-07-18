from hello_world.views import hello_world_view
from django.test import TestCase
from django.urls import resolve
from django.shortcuts import render


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, hello_world_view)

    def test_home_page_returns_correct_html(self):
        #request = self.hello_world_view(request, 'hello_world/hello.html')
        response = hello_world_view(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Hello World! Django test</title>', html)
        self.assertTrue(html.endswith('</html>'))
