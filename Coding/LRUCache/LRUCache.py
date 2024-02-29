'''
Implement a simple LRU Cache
'''
from typing import Any
class LRUCache(object):
    def __init__(self, capacity: int = 10) -> None:
        """
        the default capacity is 10 elements
        """
        self.capacity: int = capacity
        self.cache_map: dict = {}
        self.order_space: list = []

    def get_key(self, key: Any) -> Any:
        """
        if key in lru cache map, adjust the order of key, and return value, else return -1
        """
        if key in self.cache_map:
            self.order_space.remove(key)
            self.order_space.append(key)
            return self.cache_map[key]
        else:
            return -1
        
    def put_key(self, key: Any, value: Any) -> None:
        if len(self.cache_map) >= self.capacity:
            pop_key = self.order_space.pop(0)
            del self.cache_map[pop_key]
        if key in self.cache_map:
            self.order_space.remove(key)
        self.cache_map[key] = value
        self.order_space.append(key)

# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))  # Output: 1
# cache.put(3, 3)
# print(cache.get(2))  # Output: -1
# cache.put(4, 4)
# print(cache.get(1))  # Output: -1
# print(cache.get(3))  # Output: 3
# print(cache.get(4))  # Output: 4
