from django.core.cache.backends import memcached


class BMemcached(memcached.BaseMemcachedCache):
    """
    An implementation of a cache binding using python-binary-memcached
    A.K.A BMemcached.
    """
    def __init__(self, server, params):
        import bmemcached
        super(BMemcached, self).__init__(server, params,
             library=bmemcached,
             value_not_found_exception=ValueError)

    @property
    def _cache(self):
        client = getattr(self, '_client', None)
        if client:
            return client

        if self._options:
            client = self._lib.Client(self._servers,
                self._options.get('username', None),
                self._options.get('password', None))
        else:
            client = self._lib.Client(self._servers)

        self.client = client

        return client
