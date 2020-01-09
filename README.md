[![Build Status](https://secure.travis-ci.org/jaysonsantos/django-bmemcached.png?branch=master)](http://travis-ci.org/jaysonsantos/django-bmemcached)

# Django-BMemcached

A django cache backend to use [bmemcached](https://github.com/jaysonsantos/python-binary-memcached)
module which supports memcached binary protocol with authentication.

## Installing

Use pip:

```bash
pip install django-bmemcached
```

## Using

In your settings.py add bmemcached as backend:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': 'your_server:port',
    }
}
```

If you are using Django 1.11 or above, you can also add `OPTIONS` which will be
passed through to the client. The options available for `BMemcached` are as follows:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': 'your_server:port',
        'OPTIONS': {
            'username': 'user',
            'password': 'password',
            'compression': None,
            'socket_timeout': bmemcached.client.constants.SOCKET_TIMEOUT,
            'pickler': pickle.Pickler,
            'unpickler': pickle.Unpickler,
            'pickle_protocol': 0
        }
    }
}
```

NB If you have options in your configuration that are not supported (see the sample
above, or `django_bmemcached.memcached.VALID_CACHE_OPTIONS`)
the cache will raise an `InvalidCacheOptions` error the first time it is accessed:

```python
>>> from django_bmemcached import BMemcached
>>> client = BMemcached(None, {'OPTIONS': {'bad_option': True}})
>>> client.get("foo")
Traceback (most recent call last):
...
django_bmemcached.memcached.InvalidCacheOptions: Error initialising BMemcached - invalid options detected: {'bad_option'}
Please check your CACHES config contains only valid OPTIONS: {'username', 'unpickler', 'compression', 'pickle_protocol', 'password', 'pickler', 'socket_timeout'}
>>>
```

### Using in Heroku

Just add bmemcached as backend. It will work automagically if you have added memcached as Heroku addon.

```python
CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached'
    }
}
```

## Testing

```bash
DJANGO_SETTINGS_MODULE=tests.settings nosetests
```
