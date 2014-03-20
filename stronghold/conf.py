import re

from django.conf import settings


STRONGHOLD_PUBLIC_URLS = getattr(settings, 'STRONGHOLD_PUBLIC_URLS', ())
STRONGHOLD_DEFAULTS = getattr(settings, 'STRONGHOLD_DEFAULTS', True)
STRONGHOLD_PUBLIC_NAMED_URLS = getattr(settings, 'STRONGHOLD_PUBLIC_NAMED_URLS', ())

if STRONGHOLD_DEFAULTS:
    if 'django.contrib.auth' in settings.INSTALLED_APPS:
        STRONGHOLD_PUBLIC_NAMED_URLS += ('login', 'logout')

    if settings.DEBUG:
        # In Debug mode we serve the media urls as public by default as a
        # convenience. We make no other assumptions
        static_url = getattr(settings, 'STATIC_URL', None)
        media_url = getattr(settings, 'MEDIA_URL', None)

        if static_url:
            STRONGHOLD_PUBLIC_URLS += (r'^%s.+$' % static_url, )

        if media_url:
            STRONGHOLD_PUBLIC_URLS += (r'^%s.+$' % media_url, )

if STRONGHOLD_PUBLIC_URLS:
    STRONGHOLD_PUBLIC_URLS = [re.compile(v) for v in STRONGHOLD_PUBLIC_URLS]
