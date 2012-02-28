[![Build Status](https://secure.travis-ci.org/jaysonsantos/django-bmemcached.png?branch=master)](http://travis-ci.org/jaysonsantos/django-bmemcached)
# Django-BMemcached
A django cache backend to use [bmemcached] (https://github.com/jaysonsantos/python-binary-memcached) module which supports memcached binary protocol with authentication.

## Installing
Use pip:

```bash
pip install django-bmemcached
```

## Using
In your settings.py add bmemcached as backend.

```python
CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': 'your_server:port',
        'OPTIONS': {
            'username': 'user',
            'password': 'password'
        }
    }
}
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
