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

You can add a tuple of public url regexes in your settings file with the `STRONGHOLD_PUBLIC_URLS` setting.

Default setting when debug == False :
```python
STRONGHOLD_PUBLIC_URLS = ()
```

Default setting when debug == True:

```python
STRONGHOLD_PUBLIC_URLS = (
    r'^%s.+$' % settings.STATIC_URL,
    r'^%s.+$' % settings.MEDIA_URL,
    r'^%s$' % settings.LOGIN_URL,
    r'^%s$' % settings.LOGOUT_URL
)

In debug mode, we declare the common urls for your Static files, media and login/login public.

```


##Contribute

See CONTRIBUTING.md
