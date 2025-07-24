# Function to check that number entered is more than zero
def int_check(question, low):
    error = f"Please enter a number with no decimal points (not letters or anything else) that is more than or equal to {low}\n"

    while True:
        try:
            # Ask for a number with the custom prompt
            response = int(input(question))

            # Check if the number is valid
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine


width = int_check("Width: ",1)
print(width)

print()


height = int_check("Height: ", 1)
print(height)xl
