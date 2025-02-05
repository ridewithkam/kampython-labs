import math
print('Pythagorean Theorem Solver!')
print("1. Wanna solve for hypotenuse? (c)")
print("2. Wanna solve for a leg? (a or b)")
choice = input("Type 1 or 2.")

if choice == "1": # solve for hypot
    a = float(input("type side a: "))
    b = float(input("type side b: "))
    c = math.sqrt(a**2 + b**2) ## c = sqrt(a squared + b squared)
    print(f"Your Hypotenuse is {c}")

elif choice == "2":
    c = float(input("Give me your hypotenuse (c)"))
    b = float(input("Give me your leg BWAHAHA! (b)"))
    a = math.sqrt(c**2 - b**2) ## a = sqrt(c squared - b squared)
    print(f"The missing leg you have desired is {a}")

else:
    print("Stop wasting our time and pick again!")