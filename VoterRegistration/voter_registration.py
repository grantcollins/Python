'''
This program prompts user to fill out a voter registration card,
checking the inputs of the user to make sure they are eligible to vote.
'''


US_STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
             "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
             "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
citizenship = "y"
age = 0

# welcome screen
print("********************************************************\n")
print("WELCOME TO THE VOTER REGISTRATION SYSTEM")
print("enter '0' at any time to cancel registration\n")

# ask to register new voter
while True:
    new_register = input("Would you like to register as a new voter? (y or n)\n")
    if new_register == "y":
        break
    elif new_register == "n":
        break
    elif new_register == "0":
        break
    else:
        print("Invalid response. Please enter 'y' or 'n'")

# check citizenship status
print("\n" * 40)
while new_register == "y":
    print("NEW REGISTRATION\tQuestion 1 (citizenship)")
    print("enter '0' at any time to cancel registration\n")
    citizenship = input("Are you a U.S. citizen? (y or n)\n")
    if citizenship == "y":
        break
    elif citizenship == "n":
        new_register = "n"
        break
    elif citizenship == "0":
        new_register = "n"
        break
    else:
        print("Invalid response. Please enter 'y' or 'n'")

# check age
print("\n" * 40)
while new_register == "y":
    print("NEW REGISTRATION\tQuestion 2 (age)")
    print("enter '0' at any time to cancel registration\n")
    try:
        age = int(input("How old are you? (enter an integer)\n"))
        if age > 120:
            print("Ain't no way you are that old. Please enter a valid age.\n")
        elif age == 0:
            new_register = "n"
        elif age < 18:
            new_register = "n"
            break
        else:
            break
    except ValueError:
        print("Invalid response. Please enter an integer value for age")

# ask for name
print("\n" * 40)
while new_register == "y":
    print("NEW REGISTRATION\tQuestion 3 (name)")
    print("enter '0' at any time to cancel registration\n")
    first_name = input("What is your first name? (enter a string)\n")
    if first_name == "0":
        new_register = "n"
        break
    last_name = input("What is your last name? (enter a string)\n")
    if last_name == "0":
        new_register = "n"
    break

# ask for state of residence
print("\n" * 40)
while new_register == "y":
    print("NEW REGISTRATION\tQuestion 4 (state residence)")
    print("enter '0' at any time to cancel registration\n")
    state_residence = input("What state do you live in? (enter a two-letter abbreviation)\n")
    if state_residence.upper() in US_STATES:
        break
    elif state_residence == "0":
        new_register = "n"
        break
    else:
        print("Not a valid state!\n")

# ask for zip code
print("\n" * 40)
while new_register == "y":
    print("NEW REGISTRATION\tQuestion 5 (zip code)")
    print("enter '0' at any time to cancel registration\n")
    try:
        zip_code = int(input("What is your zip code? (enter a 5-digit zip)\n"))
        if len(str(zip_code)) == 5 and isinstance(zip_code, int):
            break
        elif zip_code == 0:
            new_register = "n"
            break
        else:
            print("Invalid response. Please enter a 5-digit zip\n")
    except ValueError:
        print("Invalid response. Please enter a 5-digit zip\n")

if new_register == "y":
    print("NEW REGISTRATION INFORMATION:\n")
    print("************************************************")
    print("Last name: ", last_name)
    print("First name: ", first_name)
    print("State residency: ", state_residence.upper())
    print("Zip code: ", zip_code)
    print("Citizenship: United States")
    print("************************************************\n\n")

# display message if not a U.S. citizen
if citizenship == "n":
    print("Sorry! You must be a U.S. citizen to register to vote!\n")
# display message if not 18 or older
if age < 18 and age != 0:
    print("Not old enough to vote! Please try again next election :)\n")

print("THANK YOU FOR VOTING! HAVE A NICE DAY")
