from django.test import TestCase, Client
from django.urls import reverse


class PagesTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_page(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_rules_page(self):
        response = self.client.get(reverse('pages:rules'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rules.html')
