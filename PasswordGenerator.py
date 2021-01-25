import re
import sys
import random

yes = set(['yes', 'y', 'ye'])
no = set(['no', 'n'])
mylist = []

#Accept user name. Check the input is valid or not using regex.
#If the user enters invalid input, execution will be terminated. This is achieved using sys.exit() function.
userName = raw_input("Enter the username: ").strip()
if not re.match("^[A-za-z]+$", userName):
    sys.exit("Error! Only alphabets are allowed!")
else:
    mylist.append(userName)  # If the username is valid input, add it to the list
    birthYear = raw_input("Enter the your birth year: ").strip() # Accept birth year. Check the input is valid or not using regex.
    if not re.match('^(19|20)\\d{2}$', birthYear):
        sys.exit("Error! Please enter valid birth year.")
    else:
        mylist.append(birthYear) # If the birth year is valid input, add it to the list
        choice = raw_input("Do you have a pet?" + "[Yes/No]")
        userchoice = choice.lower().strip()
        # Check if the choice entered by the user has space or it is not an appropriate choice entered by user like 'adhfds' instead of option mentioned in the yes/no list
        if userchoice.isspace() or userchoice == "" or userchoice not in yes and userchoice not in no:
            sys.exit("Please enter proper choice.")
        if userchoice in yes:
            petName = raw_input("Enter the pet name: ").strip() # Accept pet name. Check the input is valid or not using regex.
            if re.match("^[A-za-z]+$", petName):
                mylist.append(petName)  # If the birth year is valid input, add it to the list
            else:
                sys.exit("Error! Only alphabets are allowed!")
        else:
            choice1 = raw_input("Do you have a car?" + "[Yes/No]")
            userchoice1 = choice1.lower().strip()
            # Check if the choice entered by the user has space or it is not an appropriate choice entered by user like 'adhfds' instead of option mentioned in the yes/no list
            if userchoice1.isspace() or userchoice1 == "" or userchoice1 not in yes and userchoice1 not in no:
                sys.exit("Please enter proper choice.")
            if userchoice1 in yes:
                brandName = raw_input("Enter the brand name: ").strip() # Accept brand name. Check the input is valid or not using regex.
                if re.match("^[A-za-z]+$", brandName):
                    mylist.append(brandName) # If the brand name is valid input, add it to the list
                else:
                    sys.exit("Error! Only alphabets are allowed!")
            else:
                cityName = raw_input("Enter your city name: ").strip() # Accept city name. Check the input is valid or not using regex.
                if re.match("^[A-za-z]+$", cityName):
                    mylist.append(cityName) # If the city name is valid input, add it to the list
                else:
                    sys.exit("Error! Only alphabets are allowed!")

random.shuffle(mylist) #shuffle() method will be shuffle the elements present in the list.
print(mylist)
try:
    randomPassword = mylist[0] + mylist[1] + mylist[2]
    print(randomPassword)
except Exception as e:
    print(e)
