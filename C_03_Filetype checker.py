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

# Main routine goes here
while True:
    file_type = get_filetype()
    print(f"You chose {file_type}")
    if file_type == "xxx":
        print("Thanks for using the bit calculator")
        break

#ask user if "i" means image or integer
    if file_type == "i":
        wantimage = input("enter i + enter if you want image filetype, or press enter for an integer")
        if wantimage == "i":
            file_type = "image"

        else:
            file_type = "integer"

        print(f"You have chosen {file_type}")


