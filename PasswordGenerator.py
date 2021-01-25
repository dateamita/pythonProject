import re
import sys
import random

yes = set(['yes', 'y', 'ye'])
no = set(['no', 'n'])
mylist = []

userName = raw_input("Enter the username: ").strip()
if not re.match("^[A-za-z]+$", userName):
    sys.exit("Error! Only alphabets are allowed!")
else:
    mylist.append(userName)
    birthYear = raw_input("Enter the your birth year: ").strip()
    if not re.match('^(19|20)\\d{2}$', birthYear):
        sys.exit("Error! Please enter valid birth year.")
    else:
        mylist.append(birthYear)
        choice = raw_input("Do you have a pet?" + "[Yes/No]")
        userchoice = choice.lower().strip()
        if userchoice.isspace() or userchoice == "" or userchoice not in yes and userchoice not in no:
            sys.exit("Please enter proper choice.")
        if userchoice in yes:
            petName = raw_input("Enter the pet name: ").strip()
            if re.match("^[A-za-z]+$", petName):
                mylist.append(petName)
            else:
                sys.exit("Error! Only alphabets are allowed!")
        else:
            choice1 = raw_input("Do you have a car?" + "[Yes/No]")
            userchoice1 = choice1.lower().strip()
            if userchoice1.isspace() or userchoice1 == "" or userchoice1 not in yes and userchoice1 not in no:
                sys.exit("Please enter proper choice.")
            if userchoice1 in yes:
                brandName = raw_input("Enter the brand name: ").strip()
                if re.match("^[A-za-z]+$", brandName):
                    mylist.append(brandName)
                else:
                    sys.exit("Error! Only alphabets are allowed!")
            else:
                cityName = raw_input("Enter your city name: ").strip()
                if re.match("^[A-za-z]+$", cityName):
                    mylist.append(cityName)
                else:
                    sys.exit("Error! Only alphabets are allowed!")

random.shuffle(mylist)
print(mylist)
try:
    randomPassword = mylist[0] + mylist[1] + mylist[2]
    print(randomPassword)
except Exception as e:
    print(e)
