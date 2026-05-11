s = "  Hello, Python!  "
print(len(s))           # length
print(s.strip())        # remove leading/trailing whitespace
print(s.lower())        # all lowercase
print(s.upper())        # all uppercase
print(s.replace("Python", "World"))  # replace substring
print(s.split(","))     # split into list: ['  Hello', ' Python!  ']

# Indexing & slicing
text = "Python"
print(text[0])     # 'P'  (first character)
print(text[-1])    # 'n'  (last character)
print(text[0:3])   # 'Pyt' (slice)
print(text[::-1])  # 'nohtyP' (reverse)

# Concatenation
greeting = "Hello" + " " + "World"
print(greeting)  # "Hello World"    