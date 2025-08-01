def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
  Instructions:
- You will be asked to enter the type of file you want to calculate bits for.
- Supported file types:
  - Image: Calculate bits based on image dimensions (width x height x 24 bits per pixel)
  - Text: Calculate bits needed to represent ASCII text (8 bits per character)
  - Integer: Calculate bits needed to represent a positive integer in binary
- You can enter 'image', 'text', or 'integer' (or their shortcuts) when prompted.
- To exit the program, type 'xxx' when it asks for the file type :)
- If you type 'i', you will be asked to choose if you mean an image or an integer.
    ''')


# Check for file type
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # Check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response
        # Check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"
        # Check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"
        # Check for text...
        elif response in ["text", 'txt', 't']:
            return "text"
        # If the response is invalid, output an error and ask again
        else:
            print("Please choose Image, Text, or Integer, write 'xxx' to exit")


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


# Calculates number of bits needed to represent text in ascii
def calc_text_bits():
    # Get text from user
    response = input("Enter some text:  ")
    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8
    # Set up answer and return it

    answer = (f" {response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer


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


# Calculates how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to type an integer that's more than or equal to 0.
    integer = int_check("Integer: ", 0)

    # Works out and converts integer to binary, then represents it in binary digits
    raw_binary = bin(integer)

    # removes the "0b" at the beginning from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = (f"{integer} in binary is {binary}"
              f"\nWe need {num_bits} bits to represent it.")
    return answer


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key, then enter to continue ")

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()
    # Exit condition
    if file_type == "xxx":
        print("Thanks for using the bit calculator")
        break

    # Ask user if "i" means image or integer
    if file_type == "i":
        wantimage = input("Enter 'i' + enter if you want image filetype, or press enter for an integer: ")
        if wantimage == "i":
            file_type = "image"
        else:
            file_type = "integer"

    print(f"You have chosen {file_type}")

    # Run calculation based on file type
    if file_type == "text":
        text_ans = calc_text_bits()
        print(text_ans)
    elif file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        print("Invalid file type chosen.")

