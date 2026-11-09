from solution import LRUCache

def test_update_existing():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10

def test_update_refreshes():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 5)
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(1) == 5

def test_capacity_one():
    cache = LRUCache(1)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == -1
    assert cache.get("b") == 2

def test_missing():
    assert LRUCache(3).get("nope") == -1
