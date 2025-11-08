# Task 2: Numbers

# 1. Using format function to convert 145 to octal
number = 145
formatted = format(number, 'o')
print("Octal representation of 145 =", formatted)

print("-------------------------")

# 2. Calculate area of circular pond and total water
r = 84
pi = 3.14

area = pi * r * r
water_per_m2 = 1.4
total_water = area * water_per_m2

print("Area of pond =", area)
print("Total water (no decimals):", int(total_water))

print("-------------------------")

# 3. Calculate speed in meters per second
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds
print("Speed in m/s =", int(speed))
