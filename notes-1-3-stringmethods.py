# Methods (Strings)
# Author: Clinton Chieng
# Date : Feb 22, 2024

# Ask the user what iws the weather like
weather = input("What's the weather like?")
# If they reply rainy
    # Bring an umbrella
if weather.lower().strip("!,?. ") == "rainy":
    print("You'll need an umbrella!")
else:
    print(f"Sorry, I dont understand {weather}")