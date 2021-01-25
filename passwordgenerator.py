"""
This program will generate random password.
"""
import re
import sys
import random

# Create 2 lists - yes, no
# yes list will have possible options entered by user when he/she has positive response
# no list will have possible options entered by user when he/she has negative response

yes = {'yes', 'y', 'ye'}
no = {'no', 'n'}
# Create empty list
mylist = []

# Accept username and validate it using regex
userName = input("Enter the username: ").strip()
# If user enters invalid input, program execution is terminated.
if not re.match("^[A-za-z]+$", userName):
    sys.exit("Error! Only alphabets are allowed!")
else:
    mylist.append(userName)  # Add username to the mylist if the input is valid using append().
    # Accept birth year and validate it using regex
    birthYear = input("Enter the your birth year: ").strip()
    if not re.match('^(19|20)\\d{2}$', birthYear):
        sys.exit("Error! Please enter valid birth year.")
    else:
        mylist.append(birthYear)
        # Accept choice - yes or no and check if the input is present in the list - yes or no
        choice = input("Do you have a pet?" + "[Yes/No]")
        userchoice = choice.lower().strip()
        if userchoice.isspace() or userchoice == "" \
                or userchoice not in yes and userchoice not in no:
            sys.exit("Please enter proper choice.")
        if userchoice in yes:
            # Accept petName and validate it using regex
            petName = input("Enter the pet name: ").strip()
            if re.match("^[A-za-z]+$", petName):
                mylist.append(petName)
            else:
                sys.exit("Error! Only alphabets are allowed!")
        else:
            # Accept choice - yes or no and check if the input is present in the list - yes or no
            choice1 = input("Do you have a car?" + "[Yes/No]")
            userchoice1 = choice1.lower().strip()
            if userchoice1.isspace() or userchoice1 == "" \
                    or userchoice1 not in yes and userchoice1 not in no:
                sys.exit("Please enter proper choice.")
            if userchoice1 in yes:
                # Accept brandName and validate it using regex
                brandName = input("Enter the brand name: ").strip()
                if re.match("^[A-za-z]+$", brandName):
                    mylist.append(brandName)
                else:
                    sys.exit("Error! Only alphabets are allowed!")
            else:
                # Accept cityName and validate it using regex
                cityName = input("Enter your city name: ").strip()
                if re.match("^[A-za-z]+$", cityName):
                    mylist.append(cityName)
                else:
                    sys.exit("Error! Only alphabets are allowed!")
# Shuffle list using shuffle() of random module.
random.shuffle(mylist)
print(mylist)
try:
    randomPassword = mylist[0] + mylist[1] + mylist[2]
    print(randomPassword)
except Exception as exception_msg:
    print(exception_msg)