# Multiverse
# Author: Clinton
# 12 March 2024

import random

# Demonstrate some parts of the random module
# random.random() -> (0, 1.0]

def multiversal_vision():
    
    result = random.random()
    
    if result < 0.5:
        return "really bad"
    
    elif result < 0.999999:
        return "pretty bad"
    

    
    else: 
        return "decent."

input("Do you want me to see in how many timelines you succeed in life? ") 

def main():
   
    
    really_bad = 0
    pretty_bad = 0
    decent = 0 
    for _ in range(1_000_000):
        
        result = multiversal_vision()

        if result == "really bad":
            really_bad = really_bad + 1     

        elif result == "pretty bad":
            pretty_bad += 1

        else:
            decent += 1  

    print(f"really bad : {really_bad}")
    print(f"pretty bad : {pretty_bad}")
    print(f"decent. : {decent}")

main()
