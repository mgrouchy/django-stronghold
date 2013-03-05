import re

from django.core.urlresolvers import reverse
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
        STRONGHOLD_PUBLIC_URLS += (
            r'^%s.+$' % settings.STATIC_URL,
            r'^%s.+$' % settings.MEDIA_URL,
        )

STRONGHOLD_PUBLIC_URLS += [r'^%s$' % reverse(url) for url in STRONGHOLD_PUBLIC_NAMED_URLS]

if STRONGHOLD_PUBLIC_URLS:
    STRONGHOLD_PUBLIC_URLS = [re.compile(v) for v in STRONGHOLD_PUBLIC_URLS]
