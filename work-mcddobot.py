# Methods (Strings)
# Author: Clinton Chieng
# Date : Feb 22, 2024

# Ask the user if they want fries
meal = input("Do you want fries with that?")
# If they reply yes
    # give total
if meal.lower().strip("!,?. ") == "yes":
    print("Great that will be $15.75!")

elif meal.lower().strip("!,.? ") == "no":
    print("Ok that will be $12.75")
else:
    print(f"Sorry, I dont understand {meal}")