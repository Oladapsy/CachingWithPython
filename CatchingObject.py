import time

# print time to see what functions are available
# print(dir(time))

"""
This are the functions available in the time module.
We will be using time.time()
"""


class SimpleCache:
    """
    A Simple Cache class to store the time when the object is
    dropped and caught.
    """

    # init method to initialize the cache
    def __init__(self):
        self.cache = {}  # a dictionary to store the object

    def set(self, key, value, ttl):
        """
        This object will be the set function
        that accept key, value and ttl
        """
        expires_at = time.time() + ttl  # calculate the expiration time
        self.cache[key] = {
            "value": value,
            "expires_at": expires_at,
        }  # store the value and expiration time

    def get(self, key):
        """
        This object will be the get function
        that accept key and return the value if it is not expired
        """
        item = self.cache.get(key)

        if not item:
            return None

        if time.time() > item["expires_at"]:
            del self.cache[key]
            return None

        return item["value"]
    
    def evict(self, key):
        if key in self.cache:
            del self.cache[key]