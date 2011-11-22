from django.core.cache.backends import memcached


class BMemcached(memcached.BaseMemcachedCache):
    pass
