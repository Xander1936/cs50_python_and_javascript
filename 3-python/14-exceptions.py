# Exceptions: ZeroDivisionError, ValueError
# To handle exceptions, use try/except 
# -- Similar with Try/ Catch in JavaScript 
# Don't forget to import "sys"
import sys

# How to deal with exceptions
try: 
    x = int(input("x: "))
    y = int(input("y: "))

# ValueError exception:
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x/y
# Means in case of Zero Division Error:
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Means exit the program
    sys.exit(1)

print(f"{x} / {y} = {result} .")