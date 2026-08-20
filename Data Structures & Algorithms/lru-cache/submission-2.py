class LRUCache:

    """
    Given:
        constructor: init the capacity
        get: return value of the key, -1 if key not exist
        put: update the value of the key if key exists
            Otherwise, update the key-value pair to the cache
            If it reaches the capacity, remove the least recent used pair

    Difficulty:
        - how to know which is the least recent used pair?

    Approach:


    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
