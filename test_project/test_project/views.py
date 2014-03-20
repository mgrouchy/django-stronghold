from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from stronghold.decorators import public


class ProtectedView(View):
    """
    A view we want to be private
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("ProtectedView")


class PublicViewDecorator(View):
    """
    A view made public using decorator
    """
    @method_decorator(public)
    def dispatch(self, *args, **kwargs):
        return super(PublicViewDecorator, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse("PublicViewDecorator")


class PublicViewURL(View):
    """
    A view made public using the
    STRONGHOLD_PUBLIC_URLS setting
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("PublicViewURL")


class PublicViewNamedURL(View):
    """
    A view made public using the
    STRONGHOLD_PUBLIC_NAMED_URLS setting
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("PublicViewNamedURL")
