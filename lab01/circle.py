import math
print("Circle Solver!")

# get the radius from user

radius = float(input("What is your radius?"))

area = math.pi * radius ** 2 # pi times radius squared
perimeter = 2 * math.pi * radius ## perimeter

## print results    

print(f"The circle with radius {radius:.2f} has an area of {area:.2f}.")

print(f"The perimeter of the circle is {perimeter:.2f}.")

## i got in my bag with this one ;-)