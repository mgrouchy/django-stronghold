import re

from django.contrib.auth.decorators import login_required
from stronghold import conf
import stronghold

class LoginRequiredMiddleware(object):
    """
    Force all views to use login required

    View is deemed to be public if the @public decorator is applied to the view

    View is also deemed to be Public if listed in in django settings in the
    STRONGHOLD_PUBLIC_URLS dictionary
    each url in STRONGHOLD_PUBLIC_URLS must be a valid regex
    """
    def __init__(self, *args, **kwargs):
        pub_views = getattr(conf, 'STRONGHOLD_PUBLIC_URLS', ())
        self.public_view_urls = [re.compile(v) for v in pub_views]

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if request is authenticated, dont process it
        if request.user.is_authenticated():
            return None

        # if its a public view, don't process it
        is_public = getattr(view_func, 'STRONGHOLD_IS_PUBLIC', None)
        if is_public:
            return None

        # if this view matches a whitelisted regex, don't process it
        for view_url in self.public_view_urls:
            if view_url.match(request.path):
                return None

        return login_required(view_func)(request, *view_args, **view_kwargs)
