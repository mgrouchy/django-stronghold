from django.utils import unittest

from stronghold.decorators import public
from mock import Mock


class StrongholdDecoratorTestCase(unittest.TestCase):
    def test_public_decorator_sets_attr(self):
        view_func = Mock()
        view_func = public(view_func)
        is_public = getattr(view_func, 'STRONGHOLD_IS_PUBLIC', None)
        self.assertEqual(is_public, True)
