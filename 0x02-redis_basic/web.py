#!/usr/bin/env python3
""" Web module that uses the requests module to obtain the
    HTML content of a particular URL and returns it
"""


redis_store = redis.Redis()
'''The module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''A data_cacher function that caches
       the output of fetched data
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''
    A get_page function
    Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text
