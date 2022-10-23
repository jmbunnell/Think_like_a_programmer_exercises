import math
import re

# Input integer function
def get_int(prompt):
    while True:
        s = input(prompt)
        if s is None:
            return None
        if re.search(r"^[+-]?\d+$", s):
            try:
                return int(s, 10)
            except ValueError:
                pass
        
# Get input from user        
input = get_int("Number: ")    


print(f"{input}")
    

# Convert decimal to binary

# Print results