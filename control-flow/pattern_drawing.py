# pattern_drawing.py
# This program draws a square pattern using nested loops.

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop for each row
while row < size:
    # For each row, print * 'size' times without new line
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    # Increment row counter
    row += 1
