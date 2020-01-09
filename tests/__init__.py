import bz2
import os
import pickle
import unittest

import django.conf
import django.core.cache
import django_bmemcached
from django.test import override_settings
from django_bmemcached import BMemcached
from django_bmemcached.memcached import InvalidCacheOptions
from pickle import Pickler


class TestWithExplicitAuth(unittest.TestCase):
    def setUp(self):
        self.client = BMemcached(
            ('127.0.0.1:11211',),
            {'OPTIONS': {'username': 'user', 'password': 'password'}}
        )

    def tearDown(self):
        self.client.delete('key')

    def testGet(self):
        self.client.set('key', 'value')
        self.assertEqual('value', self.client.get('key'))

    def testDelete(self):
        self.client.set('key', 'value')
        self.assertEqual('value', self.client.get('key'))
        self.client.delete('key')
        self.assertEqual(None, self.client.get('key'))

    def testPropertyCacheRetunsAwaysSameServer(self):
        self.client.set('key', 'value')
        self.assertEqual(self.client._client, self.client._cache)


class TestWithTopLevelAuthParams(TestWithExplicitAuth):
    def setUp(self):
        self.client = BMemcached(
            ('127.0.0.1:11211',),
            {'USERNAME': 'user', 'PASSWORD': 'password'}
        )


class TestWithEnvironmentAuth(TestWithExplicitAuth):
    def setUp(self):
        os.environ['MEMCACHE_SERVERS'] = '127.0.0.1'
        os.environ['MEMCACHE_USERNAME'] = 'user'
        os.environ['MEMCACHE_PASSWORD'] = 'password'
        self.client = BMemcached(None, {})

    def tearDown(self):
        del os.environ['MEMCACHE_SERVERS']
        del os.environ['MEMCACHE_USERNAME']
        del os.environ['MEMCACHE_PASSWORD']


class TestWithoutAuth(TestWithExplicitAuth):
    def setUp(self):
        self.client = BMemcached(('127.0.0.1:11211',), {})


class TestPickler(Pickler):
    pass

class TestUnpickler(pickle.Unpickler):
    pass


class TestOptions(unittest.TestCase):

    # these options are all non-default - so that we can confirm that
    # they are passed through to the client.
    TEST_OPTIONS = {
        "compression": bz2,
        "pickle_protocol": 2,
        "socket_timeout": 1.0,
        "pickler": TestPickler,
        "unpickler": TestUnpickler
    }
    TEST_CACHE_CONFIG = {
        "default": {
            "BACKEND": "django_bmemcached.memcached.BMemcached",
            "BINARY": True,
            "OPTIONS": TEST_OPTIONS
        }
    }

    @unittest.skipIf(django.get_version() < '1.11', "OPTIONS did not exist pre-1.11")
    @override_settings(CACHES=TEST_CACHE_CONFIG)
    def testWithOptions(self):
        client = django.core.cache.caches["default"]
        options = self.TEST_OPTIONS
        self.assertIsInstance(client, BMemcached)
        self.assertEqual(client._cache.pickle_protocol, options["pickle_protocol"])
        self.assertEqual(client._cache.compression, options["compression"])
        self.assertEqual(client._cache.socket_timeout, options["socket_timeout"])
        self.assertEqual(client._cache.pickler, options["pickler"])
        self.assertEqual(client._cache.unpickler, options["unpickler"])

    def testInvalidOptions(self):
        """Check that InvalidCacheOptions is raised."""
        client = BMemcached(None, {'OPTIONS': {'bad_option': True}})
        with self.assertRaises(InvalidCacheOptions):
            client._cache
