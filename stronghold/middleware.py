from django.contrib.auth.decorators import login_required
from stronghold import conf, utils


class LoginRequiredMiddleware(object):
    """
    Force all views to use login required

    View is deemed to be public if the @public decorator is applied to the view

    View is also deemed to be Public if listed in in django settings in the
    STRONGHOLD_PUBLIC_URLS dictionary
    each url in STRONGHOLD_PUBLIC_URLS must be a valid regex

    """

    def __init__(self, *args, **kwargs):
        self.public_view_urls = getattr(conf, 'STRONGHOLD_PUBLIC_URLS', ())

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if request is authenticated, dont process it
        if request.user.is_authenticated():
            return None

        # if its a public view, don't process it
        if utils.is_view_func_public(view_func):
            return None

        # if this view matches a whitelisted regex, don't process it
        if any(view_url.match(request.path_info) for view_url in self.public_view_urls):
            return None

        return login_required(view_func)(request, *view_args, **view_kwargs)
