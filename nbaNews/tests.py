from datetime import datetime

from django.test import TestCase

from .models import Articles

class pageTest(TestCase):
    def setUp(self):
        Articles.objects.create(title='testTitle',content='testContent',publish_time=datetime.now())

    def test_article_can_get(self):
        article = Articles.objects.get(title='testTitle')
        self.assertEqual(article.content,'testContent')