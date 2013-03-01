import re

from django.conf import settings


STRONGHOLD_PUBLIC_URLS = getattr(settings, 'STRONGHOLD_PUBLIC_URLS', ())


if settings.DEBUG:
    # In Debug mode we serve the media urls as public by default as a
    # convenience. We make no other assumptions
    STRONGHOLD_PUBLIC_URLS += (
        r'^%s.+$' % settings.STATIC_URL,
        r'^%s.+$' % settings.MEDIA_URL,
    )


if STRONGHOLD_PUBLIC_URLS:
    STRONGHOLD_PUBLIC_URLS = [re.compile(v) for v in STRONGHOLD_PUBLIC_URLS]
