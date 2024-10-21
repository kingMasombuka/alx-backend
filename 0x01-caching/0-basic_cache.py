#!/usr/bin/python3
"""
Module for BasicCache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class definition
    """
    def put(self, key, item):
        """
        Add an item in the cache with key and data arguments
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
