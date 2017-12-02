import mock
import re

from stronghold import conf
from stronghold.middleware import LoginRequiredMiddleware

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.test import TestCase
from django.test.client import RequestFactory


class StrongholdMiddlewareTestCase(TestCase):

    def test_public_view_is_public(self):
        response = self.client.get(reverse('public_view'))
        self.assertEqual(response.status_code, 200)

    def test_private_view_is_private(self):
        response = self.client.get(reverse('protected_view'))
        self.assertEqual(response.status_code, 302)


class LoginRequiredMiddlewareTests(TestCase):

    def setUp(self):
        self.middleware = LoginRequiredMiddleware()

        self.request = RequestFactory().get('/test-protected-url/')
        self.request.user = mock.Mock()

        self.kwargs = {
            'view_func': HttpResponse,
            'view_args': [],
            'view_kwargs': {},
            'request': self.request,
        }

    def set_authenticated(self, is_authenticated):
        """Set whether user is authenticated in the request."""
        user = self.request.user
        user.is_authenticated.return_value = is_authenticated

        # In Django >= 1.10, is_authenticated acts as property and method
        user.is_authenticated.__bool__ = lambda self: is_authenticated
        user.is_authenticated.__nonzero__ = lambda self: is_authenticated

    def test_redirects_to_login_when_not_authenticated(self):
        self.set_authenticated(False)

        response = self.middleware.process_view(**self.kwargs)

        self.assertEqual(response.status_code, 302)

    def test_returns_none_when_authenticated(self):
        self.set_authenticated(True)

        response = self.middleware.process_view(**self.kwargs)

        self.assertEqual(response, None)

    def test_returns_none_when_url_is_in_public_urls(self):
        self.set_authenticated(False)
        self.middleware.public_view_urls = [re.compile(r'/test-protected-url/')]

        response = self.middleware.process_view(**self.kwargs)

        self.assertEqual(response, None)

    def test_returns_none_when_url_is_decorated_public(self):
        self.set_authenticated(False)

        self.kwargs['view_func'].STRONGHOLD_IS_PUBLIC = True
        response = self.middleware.process_view(**self.kwargs)

        self.assertEqual(response, None)

    def test_redirects_to_login_when_not_passing_custom_test(self):
        with mock.patch('stronghold.conf.STRONGHOLD_USER_TEST_FUNC', lambda u: u.is_staff):
            self.request.user.is_staff = False

            response = self.middleware.process_view(**self.kwargs)

            self.assertEqual(response.status_code, 302)

    def test_returns_none_when_passing_custom_test(self):
        with mock.patch('stronghold.conf.STRONGHOLD_USER_TEST_FUNC', lambda u: u.is_staff):
            self.request.user.is_staff = True

            response = self.middleware.process_view(**self.kwargs)

            self.assertEqual(response, None)
