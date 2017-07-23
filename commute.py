home = "you are home bla bla"
choice1 = "from home, walk or drive: "
choice2 = "from walk, bus or lirr: "
choice3 = "from lirr, subway or walk: "
choice4 = "from drive, lirr or drive: "
choice5 = "from bus, bridge or tunnel: "
choice6 = "from drive, bridge or tunnel: "
error = "error"
end = "boa, time = "

time = 0
money = 0
print(home)

user_input = input(choice1).lower()

while user_input != "walk" or "drive":
 user_input = input(choice1).lower()

 if user_input == "walk":
    user_input = input(choice2)

    if user_input == "bus":
        time = time + 30
        user_input = input(choice5)

        if user_input == "bridge":
            time = time + 60
            print(end + str(time))
        elif user_input == "tunnel":
            time = time + 75
            print(end + str(time))
        else:
            print("bridge or tunnel")

    elif user_input == "lirr":
        time = time + 45
        user_input == input(choice3)

        if user_input == "subway":
            time = time + 7
            print(end + str(time))
        elif user_input == "walk":
            time = time + 15
            print(end + str(time))
        else:
            print("subway or walk")

    else:
        print("bus or lirr")

 elif user_input == "drive":
    time = time + 10
    user_input = input(choice4)

    if user_input == "lirr":
        time = time + 40
        user_input = input(choice3)

        if user_input == "subway":
            time = time + 7
            print(end + str(time))
        elif user_input == "walk":
            time = time + 15
            print(end + str(time))
        else:
            print("subway or walk")

    elif user_input == "drive":
        user_input = input(choice6)

        if user_input == "bridge":
            time = time + 75
            print(end + str(time))
        elif user_input == "tunnel":
            time = time + 90
            print(end + str(time))
        else:
            print("bridge or tunnel")

    else:
        print("lirr or drive")

else:
    print("walk or drive")
       
