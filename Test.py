from CatchingObject import SimpleCache
import time

# use the Object
cache = SimpleCache()

# test the set
cache.set("dee", "Oladapo", 3)  # 3 seconds TTL
cache.set("jay", "John", 5)  # 5 seconds TTL

#test for get
print(cache.get("dee"), "staying for 3 seconds")         # "Oladapo"
print(cache.get("jay"), "staying for 5 seconds")         # "John"


time.sleep(4)
print()
print("After 4 seconds...")
print(cache.get("dee"), "should be expired")         # None (expired)
print(cache.get("jay"), "should still be valid")         # "John" (still valid)

# test for delete
print()
print("After deleting 'jay'...")
cache.evict("jay")

#reprint all to see the effect of delete
print("jay should now return None on call")
print("Jay:", cache.get("jay"))         # None (deleted)


