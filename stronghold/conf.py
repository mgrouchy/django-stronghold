import re

from django.core.urlresolvers import reverse, NoReverseMatch
from django.conf import settings
from django.contrib.auth.decorators import login_required


STRONGHOLD_PUBLIC_URLS = getattr(settings, 'STRONGHOLD_PUBLIC_URLS', ())
STRONGHOLD_DEFAULTS = getattr(settings, 'STRONGHOLD_DEFAULTS', True)
STRONGHOLD_PUBLIC_NAMED_URLS = getattr(settings, 'STRONGHOLD_PUBLIC_NAMED_URLS', ())
STRONGHOLD_PERMISSIONS_DECORATOR = getattr(settings, 'STRONGHOLD_PERMISSIONS_DECORATOR', login_required)


if STRONGHOLD_DEFAULTS:
    if 'django.contrib.auth' in settings.INSTALLED_APPS:
        STRONGHOLD_PUBLIC_NAMED_URLS += ('login', 'logout')
    
    # Do not login protect the logout url, causes an infinite loop
    logout_url = getattr(settings, 'LOGOUT_URL', None)
    if logout_url:
        STRONGHOLD_PUBLIC_URLS += (r'^%s.+$' % logout_url, )

    if settings.DEBUG:
        # In Debug mode we serve the media urls as public by default as a
        # convenience. We make no other assumptions
        static_url = getattr(settings, 'STATIC_URL', None)
        media_url = getattr(settings, 'MEDIA_URL', None)

        if static_url:
            STRONGHOLD_PUBLIC_URLS += (r'^%s.+$' % static_url, )

        if media_url:
            STRONGHOLD_PUBLIC_URLS += (r'^%s.+$' % media_url, )

# named urls can be unsafe if a user puts the wrong url in. Right now urls that
# dont reverse are just ignored with a warning. Maybe in the future make this
# so it breaks?
named_urls = []
for named_url in STRONGHOLD_PUBLIC_NAMED_URLS:
    try:
        url = reverse(named_url)
        named_urls.append(url)
    except NoReverseMatch:
        # print "Stronghold: Could not reverse Named URL: '%s'. Is it in your `urlpatterns`? Ignoring." % named_url
        # ignore non-matches
        pass


STRONGHOLD_PUBLIC_URLS += tuple(['^%s$' % url for url in named_urls])

if STRONGHOLD_PUBLIC_URLS:
    STRONGHOLD_PUBLIC_URLS = [re.compile(v) for v in STRONGHOLD_PUBLIC_URLS]
