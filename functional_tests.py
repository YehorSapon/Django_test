from selenium import webdriver
import unittest


class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online book shop. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/')
        # She notices the page title and header mention book shop
        self.assertIn('Ягора', self.browser.title)


if __name__ == '__main__':
    unittest.main()
