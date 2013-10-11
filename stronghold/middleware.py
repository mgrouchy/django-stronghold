from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout as auth_logout
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
        self.only_superuser = getattr(conf, 'STRONGHOLD_ONLY_SUPERUSER', False)
        self.only_staff = getattr(conf, 'STRONGHOLD_ONLY_STAFF', False)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated():
            if (self.only_superuser and not request.user.is_superuser) or (self.only_staff and not (request.user.is_staff or request.user.is_superuser)):
                auth_logout(request)
                return user_passes_test(lambda u: False)(lambda r: None)(request)
            return None

        if utils.is_view_func_public(view_func) or self.is_public_url(request.path_info):
            return None

        return login_required(view_func)(request, *view_args, **view_kwargs)

    def is_public_url(self, url):
        return any(public_url.match(url) for public_url in self.public_view_urls)
