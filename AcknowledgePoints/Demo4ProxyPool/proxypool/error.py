class ResourceDepletionError(Exception):
    def __int__(self):
        Exception.__init__(self)

    def __str__(self):
        return  repr('The proxy source is exhausted')

class PoolEmptyError(Exception):
    def __int__(self):
        Exception.__init__(self)
    def __str__(self):
        return repr('The proxy pool is empty')