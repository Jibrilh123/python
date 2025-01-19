print("Select your ride: ")
print("1. Bike ")
print("2. Car ")

choice = int(input("Enter your choice: "))

if(choice==1):
    print("What type of Bike? ")
    print("1. Scooter")
    print("2. Motorcycle")
    choice2=int(input("Enter your choice: "))
    if choice2==1:
        print("You have selected scooter")
    else:
        print("You have selected motorcycle")

elif(choice==2):
    print("What type of car? ")
    print("1. Sedan")
    print("2. SUV")
    choice3=int(input("enter your choice "))
    if choice3==1:
        print("You have selected sedan")
    else:
        print("You have selected SUV")

else:
    print("Wrong choice, Try again!")        


            