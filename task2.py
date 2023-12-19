print("welcome to the bangalore palace")
print("you are a richest person in the bangalore palace")
print("as we all know there is a one more richest person in bangalore palace  , so now u should pay to visit the bangalore palace")
print('the palace id dated ,creaky, and falling apart. you walk in the  front door')
print("do u want to enter  the balcony or food court?")

roomchoice = input(">")

if (roomchoice == "balcony"):
    print("you enterd the balcony")
    print("As u walk in ,you see a sleeping pitbull guarding some gold jewelry.")
    print("do you want to steel the gold from the pitbull?")

    pitbullchoice = input(">")
    if (pitbullchoice == "yes"):
        print("you attempt to steal the jewelry , but it wakes up and rips you to shreds.")
        print("you are dead now")
    elif (pitbullchoice == "no"):
        print("you decide to not to steal the jewelry.")
        print("you turn around and leave the house safely")


    else:
        print("invalid choice.please enter yes or no.")




elif (roomchoice == "food court"):
    print(" you choose to go into the foodcourt .")
    print("As you walk in,you see a shiny vase on the table")
    print("do you want to open the vase?")

    vasechoice = input(">")
    if (vasechoice == "yes"):
        print("you open the vase and find a pile of bones")
    elif (vasechoice == "no"):
        print("you decide not to oprn the shiny vase")
        print("As you turn to leave , you hear a creacking sound coming fromthe corner")
        print("A dark figure with glowing red eyes lanches at you , knowing you unconcinous")
        print("you wake in ur bed . it was all a dream")
    else:
        print("invalid choice , please enter yes or no")

else:
    print("invalid choice.please enter balcony or foodcourt")