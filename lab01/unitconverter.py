inches_to_centimeters = 2.54
yards_to_meters = 0.9144
ounces_to_grams = 28.3495
pounds_to_kilograms = 0.4529237

# get user input
user_input = input("Type a value with a unit (example, '1 in'): ")

# split the input for number and unit

try:
    value, unit  = user_input.split()
    value = float(value)

# conversion time boi
    if unit == "in":
        result = value * inches_to_centimeters
        print(f"{value} in = {round(result, 2)} cm")
    elif unit == "cm":
        result = value / inches_to_centimeters
        print(f"{value} cm = {round(result, 2)} in")
    elif unit == "yd":
        result = value * yards_to_meters
        print(f"{value} yd = {round(result, 2)} m")
    elif unit == "m":
        result = value / ounces_to_grams
        print(f"{value} m = {round(result, 2)} yd")
    elif unit == "oz":
        result = value * ounces_to_grams
        print(f"{value} oz = {round(result, 2)} g")
    elif unit == "g":
     result = value / ounces_to_grams
     print(f"{value} g = {round(result, 2)} oz")
    elif unit == "lb":
        result = value * pounds_to_kilograms
        print(f"{value} lb = {round(result, 2)} kg")
    elif unit == "kg":
        result = value / pounds_to_kilograms
        print(f"{value} kg = {round(result, 2)} lb")
    else:
        print("Invalid Unit. Try again!!")

except ValueError:
    print("Wrong Input! Loser!")