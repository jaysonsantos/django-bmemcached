import unittest

import django_bmemcached


class Tests(unittest.TestCase):
    def setUp(self):
        self.client = django_bmemcached.BMemcached()

    def testGet(self):
        self.assertEqual('value', self.client.get('key'))
