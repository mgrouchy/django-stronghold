.. figure:: https://travis-ci.org/mgrouchy/django-stronghold.png?branch=master
   :alt: travis

Stronghold
==========

Get inside your stronghold and make all your Django views default
login\_required

Stronghold is a very small and easy to use django app that makes all
your Django project default to require login for all of your views.

WARNING: still in development, so some of the DEFAULTS and such will be
changing without notice.

Installation
------------

Install via pip.

.. code:: sh

    pip install django-stronghold

Add stronghold to your INSTALLED\_APPS in your Django settings file

.. code:: python


    INSTALLED_APPS = (
        #...
        'stronghold',
    )

Then add the stronghold middleware to your MIDDLEWARE\_CLASSES in your
Django settings file

.. code:: python

    MIDDLEWARE_CLASSES = (
        #...
        'stronghold.middleware.LoginRequiredMiddleware',
    )

Usage
-----

If you followed the installation instructions now all your views are
defaulting to require a login. To make a view public again you can use
the public decorator provided in ``stronghold.decorators`` like so:

For function based views
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from stronghold.decorators import public


    @public
    def someview(request):
        # do some work
        #...

for class based views (decorator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from django.utils.decorators import method_decorator
    from stronghold.decorators import public


    class SomeView(View):
        def get(self, request, *args, **kwargs):
            # some view logic
            #...

        @method_decorator(public)
        def dispatch(self, *args, **kwargs):
            return super(SomeView, self).dispatch(*args, **kwargs)

for class based views (mixin)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from stronghold import StrongholdPublicMixin

    class SomeView(StrongholdPublicMixin, View):
        pass

Configuration (optional)
------------------------

STRONGHOLD\_DEFAULTS
~~~~~~~~~~~~~~~~~~~~

Use Strongholds defaults in addition to your own settings.

**Default**:

.. code:: python

    STRONGHOLD_DEFAULTS = True

You can add a tuple of url regexes in your settings file with the
``STRONGHOLD_PUBLIC_URLS`` setting. Any url that matches against these
patterns will be made public without using the ``@public`` decorator.

STRONGHOLD\_PUBLIC\_URLS
~~~~~~~~~~~~~~~~~~~~~~~~

**Default**:

.. code:: python

    STRONGHOLD_PUBLIC_URLS = ()

If STRONGHOLD\_DEFAULTS is True STRONGHOLD\_PUBLIC\_URLS contains:

.. code:: python

    (
        r'^%s.+$' % settings.STATIC_URL,
        r'^%s.+$' % settings.MEDIA_URL,
    )

When settings.DEBUG = True. This is additive to your settings to support
serving Static files and media files from the development server. It
does not replace any settings you may have in
``STRONGHOLD_PUBLIC_URLS``.

    Note: Public URL regexes are matched against
    `HttpRequest.path\_info`_.

STRONGHOLD\_PUBLIC\_NAMED\_URLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add a tuple of url names in your settings file with the
``STRONGHOLD_PUBLIC_NAMED_URLS`` setting. Names in this setting will be
reversed using ``django.core.urlresolvers.reverse`` and any url matching
the output of the reverse call will be made public without using the
``@public`` decorator:

**Default**:

.. code:: python

    STRONGHOLD_PUBLIC_NAMED_URLS = ()

If STRONGHOLD\_DEFAULTS is True additionally we search for
``django.contrib.auth`` if it exists, we add the login and logout view
names to ``STRONGHOLD_PUBLIC_NAMED_URLS``

STRONGHOLD\_USER\_TEST\_FUNC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Optionally, set STRONGHOLD_USER_TEST_FUNC to a callable to limit access to users
that pass a custom test. The callback receives a ``User`` object and should
return ``True`` if the user is authorized. This is equivalent to decorating a
view with ``user_passes_test``.

**Example**:

.. code:: python
    STRONGHOLD_USER_TEST_FUNC = lambda user: user.is_staff

**Default**:

.. code:: python
    STRONGHOLD_USER_TEST_FUNC = lambda user: user.is_authenticated


Compatiblity
------------

Tested with:

- Django 1.8.x
- Django 1.9.x
- Django 1.10.x
- Django 1.11.x
- Django 2.0.x
- Django 2.1.x
- Django 2.2.x

Contribute
----------

See CONTRIBUTING.md

.. _HttpRequest.path\_info: https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.path_info
