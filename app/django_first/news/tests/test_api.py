from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from news.models import News


class NewsApiTestCase(APITestCase):
    # def test_create_account(self):
    #     url = reverse('news-list')
    #     data = {'title': 'Новость-тест-1', 'content': 'Содержание новости тест 1'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(News.objects.count(), 1)
    #     self.assertEqual(News.objects.get().name, 'DabApps')

    def test_get(self):
        # category_1 = Category.objects.create(title='Test')
        # news_1 = News.objects.create(title='Новость-тест-1', content='Содержание новости тест 1'
        # , category_id=category_1)
        # news_2 = News.objects.create(title='Новость-тест-2', content='Содержание новости тест 2')
        # print(news_1, news_2)
        url = reverse('news-list')
        print(url)
        response = self.client.get(url, format='json')
        print(response, type(response))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(News.objects.count(), 1)
        # self.assertEqual(response.data, [])
