# Ask user for width and loop until they
# enter a number that is more than zero

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

# Calculates how many bits are needed to represent an image
def integer_calc():
    # Ask    the user to type an integer that's more than or equal to 0.
    integer = int_check("Integer: ", 0)

    #Works out and converts integer to binary, then represents it in binary digits
    raw_binary = bin(integer)

    #removes the "0b" at the beginning from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = (f"{integer} in binary is {binary}"
              f"\nWe need {num_bits} bits to represent it.")
    return answer

# Main routine goes here
integer_ans = integer_calc()
print(integer_ans)
