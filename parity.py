# Number Parity.

# Get user input
number = input("Enter a number, and I'll tell you if it's even or odd\n> ")

# Convert the input to an integer
number = int(number)

# Check if the number is even or odd
if number % 2 == 0:
    # If the number is even, print a message
    print(f"The number {number} is even.")
else:
    # If the number is odd, print a message
    print(f"The number {number} is odd.")
