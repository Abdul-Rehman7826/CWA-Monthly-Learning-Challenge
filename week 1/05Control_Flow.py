temp = 20
if temp > 30:
    print("It's hot.")
elif temp > 20:
    print("It's warm.")
elif temp > 10:
    print("It's cool.")
else:
    print("It's cold.")

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# range() for numeric loops
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # start=2, stop=10, step=2 -> 2,4,6,8
    print(i)

for num in range(10):
    if num == 3:
        continue   # skip 3
    if num == 7:
        break      # exit loop at 7
    print(num)
# Output: 0,1,2,4,5,6

