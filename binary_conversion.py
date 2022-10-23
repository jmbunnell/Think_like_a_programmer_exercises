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
print(f"{input % 2}")
    
# Convert decimal to binary
binary = []
while True:
    if input / 2 < 1:
        final = round(input % 2)
        if final > 1:
            final = 1
        binary.append(final)
        break    
    else:
        remainder = round(input % 2)
        input = input / 2
        binary.append(remainder)

# Convert integer to string
final = []
binary_final = binary.reverse()
for i in binary:
    final.append(str(i))


print(f"{binary}")
print(f"{final}")

# Print results