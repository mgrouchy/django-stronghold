#django-stronghold - Get inside your stronghold and make all your Django views default login_required 

Stronghold is a very small and easy to use django app that makes all your Django project default to require login for all of your views.


##Installation

Install via pip. 

```sh
pip install django-stronghold
```

Add stronghold to your INSTALLED_APPS in your Django settings file

```python

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
    'stronghold',
)
```

Then add the stronghold middleware to your MIDDLEWARE_CLASSES in your Django settings file

```python
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    'stronghold.middleware.LoginRequiredMiddleware',
)
```



##Contribute

See CONTRIBUTING.md
