# Creation
fruits = {"apple", "banana", "cherry"}
empty_set = set()
from_list = set([1, 2, 2, 3, 3])   # duplicates removed -> {1, 2, 3}

# Add items
fruits.add("orange")
fruits.update(["grape", "melon"])  # add multiple items

# Remove items
fruits.remove("banana")  # raises KeyError if not found

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)        # Union: {1,2,3,4,5,6}  (also a.union(b))
print(a & b)        # Intersection: {3,4}  (a.intersection(b))
print(a - b)        # Difference: {1,2}    (a.difference(b))
print(a ^ b)        # Symmetric difference: {1,2,5,6} (a.symmetric_difference(b))

print(len(fruits))   # number of unique items
print("apple" in fruits)  # True if exists, else False


s = {1, 2, 3}
s.add(4)            # {1,2,3,4}
s.remove(2)         # removes 2, KeyError if not present
s.discard(5)        # removes 5 if present, no error
popped = s.pop()    # removes and returns an arbitrary element
s.clear()

# Subset/superset
print({1,2}.issubset({1,2,3}))   # True
print({1,2,3}.issuperset({1,2})) # True
