# Creation
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []
nested = [[1, 2], [3, 4]]


nums = [3, 1, 4, 1, 5, 9]

# Access
print(nums[0])        # 3
print(nums[-1])       # 9
print(nums[1:4])      # [1, 4, 1] (slicing)

# Modify
nums[0] = 10
nums.append(2)        # add to end
nums.insert(2, 99)    # insert at index 2
nums.extend([7, 8])   # add multiple items

# Remove
nums.remove(1)        # remove first occurrence of value 1
popped = nums.pop()   # remove & return last item (or pop(index))
nums.clear()          # remove all items

# Other methods
more = [2, 7, 1, 8, 2, 8]
print(more.index(7))       # 1 (first index of 7)
print(more.count(2))       # 2 (occurrences)
more.sort()                # sorts in-place
more.sort(reverse=True)    # descending
sorted_copy = sorted(more) # returns new sorted list
more.reverse()             # reverses in-place

# Length and membership
print(len(nums))       # number of elements
print(5 in nums)       # True if 5 exists, else False

