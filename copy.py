import math
import re
from get_int import *

# Get input from user        
input = get_int("Decimal Number: ")    
#print(f"{input % 2}")
    
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
        if remainder > 1:
            remainder = 1
        binary.append(remainder)

# Convert integer to string
final = []
binary_final = binary.reverse()
for i in binary:
    final.append(str(i))

# Combine string into one variable and convert to integer
last = ''
for j in final:
    last = last + j

final_binary_int = int(last)

# Print results
#print(f"{binary}")
#print(f"{final}")
print(f"Binary Number: {final_binary_int}")

