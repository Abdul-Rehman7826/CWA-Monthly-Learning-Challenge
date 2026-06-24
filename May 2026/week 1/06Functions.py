def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!

# Multiple parameters and default values
def power(base, exponent=2):
    return base ** exponent

print(power(3))        # 9 (uses default exponent=2)
print(power(3, 3))     # 27

# Scope: variables inside a function are local
x = 10   # global variable
def func():
    x = 5   # local variable, does not change global x
    print(x)
func()     # prints 5
print(x)   # prints 10

