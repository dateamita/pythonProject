import random
import sys

yes = set(['yes', 'y', 'ye', ''])
no = set(['no', 'n'])
mylist = []
userName = raw_input("Enter the username: ")
if not userName.strip() or userName.isdigit() or userName:
    sys.exit("Please enter characters only. Spaces & Digits are not allowed")
mylist.append(userName)

try:
    birthYear = int(input("Enter the your birth year: "))
    mylist.append(str(birthYear))
except ValueError:
    print("Please enter appropriate birth year")

choice = input("Do you have a pet?" + "[Yes/No]")
userchoice = input(choice).lower()
if userchoice in yes:
    petName = input("Enter the pet name: ")
    mylist.append(petName)
else:
    choice1 = input("Do you have a car?" + "[Enter car brand name if Yes]" + "[Yes/No]")
    userchoice1 = input(choice1).lower()
    if userchoice1 in yes:
        carBrand = input("Enter the brand of the car: ")
        mylist.append(carBrand)
    else:
        cityName = input("Enter your city name")
        mylist.append(cityName)
        print(mylist)
random.shuffle(mylist)
print(mylist)
try:
    randomPassword = mylist[0] + mylist[1] + mylist[2]
    print(randomPassword)
except Exception as e:

    print(e)
