# Generates headings (eg: ---- Heading ---)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

    print('''
    - Enter an integer between 1 and 200 inclusive.
    - Enter "xxx" to exit.
    ''')


# Ask user for an integer between 1 and 200
def num_check(question):
    error = "Please enter a whole number that is between 1 and 200 inclusive\n"
    while True:
        # ask user the question, return exit code if it's been entered
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

        # if users don't enter a number, output the error message
        except ValueError:
            print(error)


def factor_finder(needs_factoring):
    all_factors = []

    # find square root of number to be factored so that our loop is efficient.
    stop_raw = needs_factoring ** 0.5
    stop = int(stop_raw + 1)

    # loop and check each number from one upwards to check if it's a
    # factor.  Stop when we get to the square root of the number (ie: 'half way')
    for item in range(1, stop):
        num_left = needs_factoring % item
        # If number fits evenly it will add it to the list
        if num_left == 0:
            all_factors.append(item)

            # retrieve the second 'partner' factor as an integer
            partner = to_factor // item

            # only add factor to list if it is not already in the list
            if partner not in all_factors:
                all_factors.append(partner)

    # finds out if the number is unity
    if len(all_factors) == 1:
        comment = "\n1 is UNITY (has only one factor, itself)."

    # Finds out if the number is a prime number.
    elif len(all_factors) == 2:
        comment = f"\n{to_factor} is a prime number."

    # Finds out if the number is a perfect square and outputs it.
    elif len(all_factors) % 2 == 1:
        comment = f"\n{to_factor} is a perfect square."

    # If the number is nothing special this outputs it.
    else:
        comment = ""

    print(f"{comment}")

    all_factors.sort()

    if len(all_factors) > 1:
        print(f"The factors of {to_factor} are: {all_factors}\n")


# Main routine goes here
statement_generator("The Ultimate Factor Finder", "-")

# Displays instructions if requested
want_instructions = input("\nPress <enter> to read the instructions: ")

if want_instructions == "":
    instructions("Instructions", "-")

while True:

    # ask the user for the number to be factorised
    to_factor = num_check("Enter a number to factor: ")

    if to_factor == "xxx":
        break

    else:
        factor_finder(to_factor)

print("Thank you for using the factors calculator")
