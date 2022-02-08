from django.test import TestCase, RequestFactory
from django.urls import resolve

from news.views import index


class NewsURLsTestCase(TestCase):
    def test_news_url_uses_index_view(self):
        root = resolve('/news/')
        self.assertEqual(root.func, index)


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_basic(self):
        request = self.factory.get('/news/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
