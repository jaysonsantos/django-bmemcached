import os
from django.core.cache.backends import memcached


class BMemcached(memcached.BaseMemcachedCache):
    """
    An implementation of a cache binding using python-binary-memcached
    A.K.A BMemcached.
    """
    def __init__(self, server, params):
        import bmemcached
        params.setdefault('OPTIONS', {})

        username = params['OPTIONS'].get('username', params.get('USERNAME', os.environ.get('MEMCACHE_USERNAME')))

        if username:
            params['OPTIONS']['username'] = username

        password = params['OPTIONS'].get('password', params.get('PASSWORD', os.environ.get('MEMCACHE_PASSWORD')))

        if password:
            params['OPTIONS']['password'] = password

        if not server:
            server = tuple(os.environ.get('MEMCACHE_SERVERS', '').split(','))

        super(BMemcached, self).__init__(server, params, library=bmemcached, value_not_found_exception=ValueError)

    def close(self, **kwargs):
        # Override base behavior of disconnecting from memcache on every HTTP request.
        # This method is, in practice, only called by Django on the request_finished signal
        pass

    @property
    def _cache(self):
        client = getattr(self, '_client', None)
        if client:
            return client

        if self._options:
            client = self._lib.Client(
                self._servers, self._options.get('username', None),
                self._options.get('password', None)
            )
        else:
            client = self._lib.Client(self._servers,)

        self._client = client

        return client
