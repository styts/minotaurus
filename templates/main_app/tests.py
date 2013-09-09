from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):
    def test(self):
        response = self.client.get(reverse('home'))
        assert "Hello World!" in response.content
