from django.core.urlresolvers import reverse

from django.utils import unittest
from django.test.client import Client


class StrongholdMiddlewareTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.public_url = reverse("public_view")
        cls.private_url = reverse("protected_view")

    def test_public_view_is_public(self):
        client = Client()
        response = client.get(self.public_url)
        self.assertEqual(response.status_code, 200)

    def test_private_view_is_private(self):
        client = Client()
        response = client.get(self.private_url)
        self.assertEqual(response.status_code, 302)
