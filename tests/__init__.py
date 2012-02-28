import os
import unittest

import django_bmemcached


class TestWithExplicitAuth(unittest.TestCase):
    def setUp(self):
        self.client = django_bmemcached.BMemcached(('127.0.0.1:11211', ),
            {'OPTIONS': {'username': 'user', 'password': 'password'}})

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


class TestWithEnvironmentAuth(TestWithExplicitAuth):
    def setUp(self):
        os.environ['MEMCACHE_SERVERS'] = '127.0.0.1'
        os.environ['MEMCACHE_USERNAME'] = 'user'
        os.environ['MEMCACHE_PASSWORD'] = 'password'
        self.client = django_bmemcached.BMemcached(None, {})

    def tearDown(self):
        del os.environ['MEMCACHE_SERVERS']
        del os.environ['MEMCACHE_USERNAME']
        del os.environ['MEMCACHE_PASSWORD']


class TestWithoutAuth(TestWithExplicitAuth):
    def setUp(self):
        self.client = django_bmemcached.BMemcached(('127.0.0.1:11211', ), {})
