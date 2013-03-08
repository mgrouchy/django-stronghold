import mock

from stronghold.middleware import LoginRequiredMiddleware

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.test import TestCase
from django.test.client import RequestFactory


class StrongholdMiddlewareTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.public_url = reverse("public_view")
        cls.private_url = reverse("protected_view")

    def test_public_view_is_public(self):
        response = self.client.get(self.public_url)
        self.assertEqual(response.status_code, 200)

    def test_private_view_is_private(self):
        response = self.client.get(self.private_url)
        self.assertEqual(response.status_code, 302)


class LoginRequiredMiddlewareTests(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('/')
        self.request.user = mock.Mock()

        self.kwargs = {
            'view_func': HttpResponse,
            'view_args': [],
            'view_kwargs': {},
            'request': self.request,
        }

    def test_redirects_to_login_when_not_authenticated(self):
        self.request.user.is_authenticated.return_value = False

        response = LoginRequiredMiddleware().process_view(**self.kwargs)

        self.assertEqual(response.status_code, 302)

    def test_returns_none_when_authenticated(self):
        response = LoginRequiredMiddleware().process_view(**self.kwargs)

        self.assertEqual(response, None)
