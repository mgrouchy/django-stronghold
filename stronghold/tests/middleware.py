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

    def test_redirects_to_login_when_not_authenticated(self):
        request = RequestFactory().get('/')
        request.user = mock.Mock()
        request.user.is_authenticated.return_value = False

        response = LoginRequiredMiddleware().process_view(
            request=request,
            view_func=HttpResponse,
            view_args=[],
            view_kwargs={}
        )

        self.assertEqual(response.status_code, 302)
