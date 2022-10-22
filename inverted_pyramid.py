# Create a inverted pyramid with hashmarks

########
 ######
  ####
   ##

# Base of 8; minus 2 hashes and add 1 space each side per line; end with 2 hashes - height: 4 lines & width: 8 characters

# Get integer input from user
while True:
    prompt = int(input("Height: "))
    if prompt > 0 and prompt < 9:
        break


# Print out hash marks and spaces
row_count = prompt * 2
for row in range(1, prompt + 1):
    print(" " * (row - 1) + "#" * (row_count) + " " * (row - 1))
    row_count = row_count - 2
    