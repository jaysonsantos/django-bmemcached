import unittest

import django_bmemcached


class Tests(unittest.TestCase):
    def setUp(self):
        self.client = django_bmemcached.BMemcached(('127.0.0.1:11211', ),
            {'OPTIONS': {'username': 'user', 'password': 'password'}})

    def testGet(self):
        self.assertEqual('value', self.client.get('key'))
