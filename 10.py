# Round floating-point numbers

# Task: Given a floating-point number value
# Round value to the nearest integer.
# Round value to two decimal places.
# value:float = 12.34567
# Expected Output:
# Rounded to nearest integer: 12
# Rounded to two decimal places: 12.35


# Solution:



value:float = 12.34567

rounded_integer = round(value)

rounded_two_decimals = round(value, 2)

print(f"Rounded to nearest integer: {rounded_integer}")
print(f"Rounded to two decimal places: {rounded_two_decimals}")


