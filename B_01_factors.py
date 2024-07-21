# Generates headings (eg: ---- Heading ---)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

    print('''
Enter a valid number to factor:
To exit factor calculator enter:
    - xxx
    ''')


# Ask user for an integer between 1 and 200
def num_check(question):
    error = "Please enter a whole number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask user for a number
            response = int(response)

            # enter a number that is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

statement_generator("The Ultimate Factor Finder", "-")

# Displays instructions if requested
want_instructions = input("\n Press <enter> to read the instructions")


if want_instructions == "":
    instructions("Instructions", "-")

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
