# A simple In-Memory cache

## Introduction

This is a simple In-memory cache implemented in Python using a Linked List and Hash Map to support put and get operations in O(1) time. 

Currently, it supports one eviction policy which is the "Least Recently Used" (LRU) but can be extended to support multiple eviction policies.

## Usage with example

```
//this will initialize a new cache object
newCache = _cache(cache_size, eviction_policy) --> e.g., newCache = _cache(10, "LRU") 

//putting a key-value pair into the cache
newCache.put(key, value)  --> e.g., newCache.put("key1", "value123")

//getting the value from cache
newCache.get(key)  --> e.g., newCache.get("key1")  --> returns "value123"

