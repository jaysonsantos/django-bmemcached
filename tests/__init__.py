import unittest

import django_bmemcached


class Tests(unittest.TestCase):
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
