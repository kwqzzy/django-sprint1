from django.test import TestCase, Client
from django.urls import reverse


class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail_page(self):
        response = self.client.get(reverse('blog:post_detail', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')

    def test_category_page(self):
        response = self.client.get(reverse('blog:category_posts', args=['travel']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
