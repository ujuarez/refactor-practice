from budgetFunction import budgetFunction
from calculator import calculator, add
from weather_advice import weather_advice
from weather_advice import weather_advice
from shopping_list import shopping_list
from TemperatureConverter import TemperatureConverter
from InventoryFunction import InventoryFunction
from validate_password import validate_password

# Create a Function: Turn this logic into a function called suggest_destination(budget) that:

# Accepts budget as an argument.
# Returns the suggestion as a string.

# # ORIGINAL #
# if budget < 100:
#             return "Local day trips."
#         elif budget < 500:
#             return "Nearby cities."
#         else:
#             return "International travel!"


print(budgetFunction(300))


# Instructions for Students:

# Refactor this code by creating a function for each arithmetic operation (e.g., add, subtract, etc.).
# Make a Calculator class that contains these functions as methods.
# Ensure that division checks for zero before attempting the operation.
# Move the arithmetic logic into a file named calculator.py.

# # ORIGINAL #
# a = 10
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# if b != 0:
#     print(a / b)
# else:
#     print("Cannot divide by zero")


print(calculator(10, 5))
print(add(10,5))


####################################################################################################
# Instructions for Students:

# Create a function that takes weather as an argument and returns the appropriate advice.
# Optionally, create a class WeatherAssistant with a method for weather advice.
#Move the weather advice logic into a file named weather_advice.py.

# # ORIGINAL #
# weather = "rainy"
# if weather == "rainy":
#     print("Take an umbrella.")
# elif weather == "sunny":
#     print("Wear sunglasses.")
# elif weather == "cold":
#     print("Wear a jacket.")
# else:
#     print("Weather unknown. Dress comfortably.")


print(weather_advice("rainy"))


# Instructions for Students:

# Refactor this code by creating functions to:
# Add an item to the shopping list.
# Remove an item from the shopping list.
# Print all items in the shopping list.
# Optionally, create a ShoppingList class that manages the list with the above methods.
#Move the shopping list logic into a file named shopping_list.py.

# # ORIGINAL #
# shopping_list = ["apples", "bananas", "carrots"]
# shopping_list.append("dates")
# shopping_list.remove("bananas")
# for item in shopping_list:
#     print(item)


print(shopping_list("apples"))


# Instructions for Students:

# Refactor this code by creating two functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Consider creating a TemperatureConverter class with these methods.

# # ORIGINAL #
# celsius = 25
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C is {fahrenheit}°F")

# fahrenheit = 77
# celsius = (fahrenheit - 32) * 5/9
# print(f"{fahrenheit}°F is {celsius}°C")


print(TemperatureConverter(25))


# Instructions for Students:

# Create functions for:
# Adding an item to the inventory.
# Removing an item from the inventory.
# Printing the inventory.
# Optionally, organize these into an Inventory class.

# # ORIGINAL #
# inventory = {}
# inventory["apples"] = 10
# inventory["bananas"] = 5
# inventory["apples"] -= 3
# if inventory["apples"] <= 0:
#     del inventory["apples"]
# print(inventory)


print(InventoryFunction(10))


# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.

# # ORIGINAL #
# password = "Pass1234"
# if len(password) >= 8:
#     if any(char.isdigit() for char in password):
#         if any(char.isupper() for char in password):
#             print("Strong password")
#         else:
#             print("Password needs an uppercase letter")
#     else:
#         print("Password needs a number")
# else:
#     print("Password is too short")


print(validate_password("Pass1234"))