
def statement_generator (statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")
# Displays instructions

def instructions():
    statement_generator("Instructions", "-")

    print('''
  Instructions:
  -task1
  -task2
  -task3
    ''')

    


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions " 
                          "or any key, then enter to continue ")

if want_instructions == "":
    instructions()