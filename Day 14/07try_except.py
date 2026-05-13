""""This code demonstrates the use of try-except blocks to handle exceptions that may occur during 
    user input and division operations. 
    It includes handling for ValueError when non-numeric input is provided and ZeroDivisionError 
    when attempting to divide by zero. 
    The finally block ensures that a message is printed after each calculation attempt, 
    regardless of whether an exception occurred or not.

"""
def divide():
    try:
        a = float(input("Numerator: "))
        b = float(input("Denominator: "))
        result = a / b
    except ValueError:
        print("Please enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("Calculation attempt finished.\n")

# Run it multiple times
for _ in range(3):
    divide()