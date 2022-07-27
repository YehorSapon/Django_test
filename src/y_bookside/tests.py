from django.test import TestCase
from django.urls import resolve
from .views import home_page
from .models import PublishingHous


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page(request))

    def test_home_page_returns_correct_html(self):
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Кнігі ў Ягора</title>', html)
        self.assertTrue(html.endswith('</html>'))


class ModelTest(TestCase):

    def test_publishinghouse_model_save_and_retrieve(self):
        publ_house1 = PublishingHous(
            name='PublishingHous1',
            description='description of PublishingHous1'
        )
        publ_house1.save()

        all_publihinghouse = PublishingHous.objects.all()
        self.assertEqual(len(all_publihinghouse), 1)
        self.assertEqual(publ_house1[0].name, publ_house1.name)

        self.fail('Finish the test!')
