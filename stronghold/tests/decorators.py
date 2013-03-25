import functools

from stronghold import decorators

from django.utils import unittest


class StrongholdDecoratorTests(unittest.TestCase):

    def test_public_decorator_sets_attr(self):
        @decorators.public
        def function():
            pass

        self.assertTrue(function.STRONGHOLD_IS_PUBLIC)

    def test_public_decorator_sets_attr_with_nested_decorators(self):
        def stub_decorator(func):
            return func

        @decorators.public
        @stub_decorator
        def inner_function():
            pass

        self.assertTrue(inner_function.STRONGHOLD_IS_PUBLIC)

    def test_public_decorator_works_with_partials(self):
        def function():
            pass
        partial = functools.partial(function)

        decorators.public(partial)

        self.assertTrue(function.STRONGHOLD_IS_PUBLIC)
