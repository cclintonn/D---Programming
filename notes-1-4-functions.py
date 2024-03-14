# Functions
# Clinton Chieng
# Feb 26, 2024


# Create a function called say_hello
#   It's going to print "Hello"

def say_hello():
    print("Hello!")


# Create a function called say_hello_params
#   Print "Hello {parameter}!"
    
def say_hello_params(name):
    print(f"Hello {name}!")

# Create a function called how_big
# It takes a number as an input/param
#   It returns how big the number is
def how_big(num):
    if num < 0:
        return"Very Small"
    if num < 10:
        return"Pretty Small"
    if num < 100:
        return"Small"
    if num < 1000:
        return "Pretty Big"
    return"Really Big"





# # say_hello()
# # say_hello_params("Clinton")
# print(how_big(10))

# result = how_big(1_000_000)
# print(result)