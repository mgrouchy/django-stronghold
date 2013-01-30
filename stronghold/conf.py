from django.conf import settings

if settings.DEBUG:
	# In Debug mode we serve the media urls as public by default
	STRONGHOLD_PUBLIC_URLS = (r'^/static/.+$', r'^/media/.+$')
else:
	# make no such assumptions in production
	STRONGHOLD_PUBLIC_URLS = ()


STRONGHOLD_PUBLIC_URLS = getattr(settings, 'STRONGHOLD_PUBLIC_URLS', STRONGHOLD_PUBLIC_URLS)
