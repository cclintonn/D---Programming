# Notes - Dictionaries

# Big Ideas:
#   - A dictionary is a data structure 
#   - Dictionaries map keys to values

# Flashback to lists
person = ["John","23 years old","4500 1023 2222 1111"]

# Rewrite person as a dictionary
person_dict = {
    "name": "John",
    "age": "23 years old",
    "cc num": "4500 1023 2222 1111"
}

person_one = {
    "name": "Jim", 
    "age": "42",
    "cc num": "5100 2030 3884 1992"
}

# Get and print the person's name(?)
# print(person[0]) # use the index

# print(person[2])  # last item in the list
# print(person[-1]) # start counting from end

# print(person[10]) # code will break

# Grab values from a dictionary
print(person_dict["name"])
print(person_dict["cc num"])