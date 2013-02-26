from django.conf import settings


if settings.DEBUG:
    # In Debug mode we serve the media urls as public by default
    # We should also serve the login/logout pages as public
    STRONGHOLD_PUBLIC_URLS = (
        r'^%s.+$' % settings.STATIC_URL,
        r'^%s.+$' % settings.MEDIA_URL,
        r'^%s$' % settings.LOGIN_URL,
        r'^%s$' % settings.LOGOUT_URL,
    )
else:
    # make no such assumptions in production
    STRONGHOLD_PUBLIC_URLS = ()


STRONGHOLD_PUBLIC_URLS = getattr(settings,
                                 'STRONGHOLD_PUBLIC_URLS',
                                 STRONGHOLD_PUBLIC_URLS)
