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
def image_calc():
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # Calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} × 24 = {num_bits}")
    return answer

# Main routine goes here
image_ans = image_calc()
print(image_ans)
