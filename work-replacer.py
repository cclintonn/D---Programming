# replacer
# Clinton Chieng
# Feb 26, 2024

# # Create a function called main
# #   Prompt the user to type something in
# #   Use the translate function on the user input
# #   Print the result

def main():
    text = input("Say something! ")
    print(translate(text))


# Create a function called translate
#   Accepts a string
#   Replace all 100 with 💯
#   Replace all noodles with 🍜
#   Return the result

def translate(text: str):
    return text.replace("100", "💯").replace("noodles", "🍜")

main()