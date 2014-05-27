from stronghold import conf, utils


class LoginRequiredMiddleware(object):
    """
    Force all views to use the permissions defined by
    STRONGHOLD_PERMISSIONS_DECORATOR. Default is login_required, but can use
    staff_member_required or a user defined decorator

    View is deemed to be public if the @public decorator is applied to the view

    View is also deemed to be Public if listed in in django settings in the
    STRONGHOLD_PUBLIC_URLS dictionary
    each url in STRONGHOLD_PUBLIC_URLS must be a valid regex

    """

    def __init__(self, *args, **kwargs):
        self.public_view_urls = getattr(conf, 'STRONGHOLD_PUBLIC_URLS', ())

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated() or utils.is_view_func_public(view_func) \
                or self.is_public_url(request.path_info):
            return None

        return conf.STRONGHOLD_PERMISSIONS_DECORATOR(view_func)(request, *view_args, **view_kwargs)

    def is_public_url(self, url):
        return any(public_url.match(url) for public_url in self.public_view_urls)
