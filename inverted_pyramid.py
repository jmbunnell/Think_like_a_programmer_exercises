# Create a inverted pyramid with hashmarks

########
 ######
  ####
   ##

# Base of 8; minus 2 hashes and add 1 space each side per line; end with 2 hashes - height: 4 lines & width: 8 characters

# Get integer input from user
input = int(input("Height: "))
print(f"{input}")

# Print out 8 hashmarks on same line
first_value = input * 2
for i in range(input):
   print('#' * first_value)