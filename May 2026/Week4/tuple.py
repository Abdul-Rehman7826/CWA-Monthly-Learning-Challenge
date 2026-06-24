# Creation
point = (3, 4)
colors = "red", "green", "blue"   # parentheses optional
single_item_tuple = (5,)          # comma needed for one element
empty = ()

# Immutability: you cannot add, remove, or change items.
# point[0] = 10   # TypeError: 'tuple' object does not support item assignment
print(point[0])  # 3
print(point)     # (3, 4)

print(colors)    # ('red', 'green', 'blue')
print(single_item_tuple)  # (5,)


t = (1, 2, 3, 2, 2)
print(len(t))
print(t.count(2))     # 3
print(t.index(3))     # 2

# Unpacking
a, b, c, *rest = t    # a=1, b=2, c=3, rest=[2,2]
x, y = (10, 20)       # x=10, y=20
print(a, b, c, rest)  # 1 2 3 [2, 2]
