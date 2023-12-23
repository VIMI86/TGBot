import unittest
from unittest.mock import patch
from B import *


class TestNews(unittest.TestCase):
    @patch('B.requests.get')
    def test_news_true(self, getmock):
        getmock.return_value.json.return_value = {
            'articles': [
                {'title': 'Новость 1', 'url': 'http://news.com/news/1', 'publishedAt': '2023-12-12'}
            ]
        }
        result = news()
        expected_result = 'Новость 1\nhttp://news.com/news/1\n2023-12-12'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()