from stronghold.views import StrongholdPublicMixin

import django
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

if django.VERSION[:2] < (1, 9):
    from django.utils import unittest
else:
    import unittest


class StrongholdMixinsTests(unittest.TestCase):

    def test_public_mixin_sets_attr(self):

        class TestView(StrongholdPublicMixin, View):
            pass

        self.assertTrue(TestView.dispatch.STRONGHOLD_IS_PUBLIC)

    def test_public_mixin_sets_attr_with_multiple_mixins(self):

        class TestView(StrongholdPublicMixin, TemplateResponseMixin, View):
            template_name = 'dummy.html'

        self.assertTrue(TestView.dispatch.STRONGHOLD_IS_PUBLIC)
