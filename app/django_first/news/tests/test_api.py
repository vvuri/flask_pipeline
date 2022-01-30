from django.urls import reverse
from rest_framework.test import APITestCase


class NewsApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('news-list')
        print(url)
        response = self.client.get(url)
        print(response)
