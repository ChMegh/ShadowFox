# Task 1: Variables

# 1. Create a variable named pi and store value 22/7
pi = 22/7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

print("----------------------")

# 2. Trying to create a variable named 'for'
# This will cause a syntax error because 'for' is a keyword in Python
# for = 4  #  This will not work

# Correct way:
for_value = 4
print("Correct variable name:", for_value)

print("----------------------")

# 3. Simple Interest Calculation
P = 10000  # principal amount
R = 5      # interest rate
T = 3      # time in years

simple_interest = (P * R * T) / 100
print("Simple Interest for 3 years =", simple_interest)
