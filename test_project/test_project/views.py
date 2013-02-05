from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from stronghold.decorators import public


class ProtectedView(View):
    """A view we want to be private"""
    def get(self, request, *args, **kwargs):
        return HttpResponse("ProtectedView")


class PublicView(View):
    """ A view we want to be public"""
    @method_decorator(public)
    def dispatch(self, *args, **kwargs):
        return super(PublicView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("PublicView")
