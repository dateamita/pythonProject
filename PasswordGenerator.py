import re
import sys
import random

yes = set(['yes', 'y', 'ye'])
no = set(['no', 'n'])
mylist = []

userName = raw_input("Enter the username: ")
if not re.match("^[a-z]+$", userName):
    sys.exit("Error! Only letters a-z allowed!")
else:
    mylist.append(userName)
    birthYear = raw_input("Enter the your birth year: ")
    if not re.match('^[0-9]+$', birthYear):
        sys.exit("Error! Only numbers 0-9 allowed!")
    else:
        mylist.append(birthYear)
        choice = raw_input("Do you have a pet?" + "[Yes/No]")
        userchoice = choice.lower()
        if userchoice in yes:
            petName = raw_input("Enter the pet name: ")
            if re.match("^[a-z]+$", petName):
                mylist.append(petName)
            else:
                sys.exit("Error! Only letters a-z allowed!")
        else:
            choice1 = raw_input("Do you have a car?" + "[Enter car brand name if Yes]" + "[Yes/No]")
            userchoice1 = choice1.lower()
            if userchoice1 in yes:
                brandName = raw_input("Enter the brand name: ")
                if re.match("^[a-z]+$", brandName):
                    mylist.append(brandName)
                else:
                    sys.exit("Error! Only letters a-z allowed!")
            else:
                cityName = raw_input("Enter your city name")
                if re.match("^[a-z]+$", cityName):
                    mylist.append(cityName)
                else:
                    sys.exit("Error! Only letters a-z allowed!")

random.shuffle(mylist)
print(mylist)
try:
    randomPassword = mylist[0] + mylist[1] + mylist[2]
    print(randomPassword)
except Exception as e:
    print(e)
