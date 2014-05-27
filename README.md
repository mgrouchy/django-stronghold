![travis](https://travis-ci.org/mgrouchy/django-stronghold.png?branch=master)

#Stronghold

Get inside your stronghold and make all your Django views default login_required

Stronghold is a very small and easy to use django app that makes all your Django project default to require login for all of your views.

WARNING: still in development, so some of the DEFAULTS and such will be changing without notice.

##Installation

Install via pip.

```sh
pip install django-stronghold
```

Add stronghold to your INSTALLED_APPS in your Django settings file

```python

INSTALLED_APPS = (
    #...
    'stronghold',
)
```

Then add the stronghold middleware to your MIDDLEWARE_CLASSES in your Django settings file

```python
MIDDLEWARE_CLASSES = (
    #...
    'stronghold.middleware.LoginRequiredMiddleware',
)

```

##Usage

If you followed the installation instructions now all your views are defaulting to require a login.
To make a view public again you can use the public decorator provided in `stronghold.decorators` like so:

###For function based views
```python
from stronghold.decorators import public


@public
def someview(request):
	# do some work
	#...

```

###for class based views

```python
from django.utils.decorators import method_decorator
from stronghold.decorators import public


class SomeView(View):
	def get(self, request, *args, **kwargs):
		# some view logic
		#...

	@method_decorator(public)
	def dispatch(self, *args, **kwargs):
    	return super(SomeView, self).dispatch(*args, **kwargs)
```

##Configuration (optional)


###STRONGHOLD_DEFAULTS

Use Strongholds defaults in addition to your own settings.

**Default**:

```python
STRONGHOLD_DEFAULTS = True
```

You can add a tuple of url regexes in your settings file with the
`STRONGHOLD_PUBLIC_URLS` setting. Any url that matches against these patterns
 will be made public without using the `@public` decorator.


###STRONGHOLD_PUBLIC_URLS

**Default**:
```python
STRONGHOLD_PUBLIC_URLS = ()
```

If STRONGHOLD_DEFAULTS is True STRONGHOLD_PUBLIC_URLS contains:
```python
(
    r'^%s.+$' % settings.STATIC_URL,
    r'^%s.+$' % settings.MEDIA_URL,
)

```
When settings.DEBUG = True. This is additive to your settings to support serving
Static files and media files from the development server. It does not replace any
settings you may have in `STRONGHOLD_PUBLIC_URLS`.

> Note: Public URL regexes are matched against [HttpRequest.path_info](https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.path_info).

###STRONGHOLD_PUBLIC_NAMED_URLS
You can add a tuple of url names in your settings file with the
`STRONGHOLD_PUBLIC_NAMED_URLS` setting. Names in this setting will be reversed using
`django.core.urlresolvers.reverse` and any url matching the output of the reverse
call will be made public without using the `@public` decorator:

**Default**:
```python
STRONGHOLD_PUBLIC_NAMED_URLS = ()
```

If STRONGHOLD_DEFAULTS is True additionally we search for `django.contrib.auth`
if it exists, we add the login and logout view names to `STRONGHOLD_PUBLIC_NAMED_URLS`

###STRONGHOLD_PERMISSIONS_DECORATOR
Optionally configure STRONGHOLD_PERMISSIONS_DECORATOR to be something besides
`login_required`. This allows the developer to set this to an alternative
decorator like `staff_member_required` or a user created decorator that
processes a view function and returns `None` or a `HTTPResponse`.

**Default**:
```python
STRONGHOLD_PERMISSIONS_DECORATOR = login_required
```

##Compatiblity

Tested with:
* Django 1.4.x
* Django 1.5.x
* Django 1.6.x

##Contribute

See CONTRIBUTING.md
