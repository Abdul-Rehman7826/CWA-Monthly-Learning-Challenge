# Creation
person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
empty = {}
using_dict = dict(name="Bob", age=25)    # keyword arguments
pairs = dict([("a", 1), ("b", 2)])       # list of tuples

person = {"name": "Alice", "age": 30}

# Access
print(person["name"])         # "Alice"  (KeyError if missing)
print(person.get("age"))      # 30
print(person.get("city", "Unknown"))  # "Unknown" (default if key not found)

# Add/update
person["city"] = "Paris"      # add new key
person["age"] = 31            # update existing key
# Merge using update
person.update({"age": 32, "job": "Engineer"})

print(person.get("city", "Unknown"))  # "Paris"
print(person)  # {'name': 'Alice', 'age': 32, 'city': 'Paris', 'job': 'Engineer'}