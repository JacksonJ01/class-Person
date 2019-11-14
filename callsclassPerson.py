# Jackson J.
# 11/13/19
# I will create the basis for a project I have had on my mind for a while
from classPerson import Person
from random import *

input("PRESS ENTER")
print('We\'re gonna make 2 people. And see what they do.')
print("But before we do that, should we separate them, or let them socialize?")
separate = input(">>>").title()
if separate == "Socialize" or separate == "Separate" or separate == "Se" or separate == "So":
    print("That choice will impact your decision later on")

else:
    while separate != "Socialize" or separate != "Separate" or separate != "Se" or separate != "So":
        print("Sorry, can you retype that?")
        print('You can even do "se" for separate and "so" for socialize')
        separate = input(">>>").title()
        if separate == "Socialize" or separate == "Separate" or separate == "Se" or separate == "So":
            print("That choice will impact your decision later on")
            break

print("What do you want to name this person?")
name = input(">>>").title()
print("Okay. How old is that person?")
age = input(">>>")
print("Alright, now, in inches, how tall is this person?")
height = input(">>>")
print("And what is the weight of the person?")
weight = input(">>>")
print("How strong, in numbers, is your person?")
strength = input(">>>")
Person1 = Person(name, age, height, weight, strength)

input("PRESS ENTER TO ENTER THOSE VALUES")
Person1.person_des()

print("\nNow for the second person. What will their attributes be.")
print("Name:")
name2 = input(">>>").title()
print("Age:")
age2 = input(">>>")
print("Weight in pounds:")
weight2 = input(">>>")
print("And the Height in inches:")
height2 = input(">>>")
print('And the strength for this person is:')
strength = input(">>>")
Person2 = Person(name2, age2, height2, weight2, strength)

print(f"\nSo we have {Person1.name} and {Person2.name}")
if separate == "Separate" or separate == "Se":
    print("Hm, they seem lonely. You decided to separate them. They could have started a civilation.")
    print("At least they aren't able to fight each other. That's good.")
    exit()

elif separate == "Socialize" or separate == "So":
    print("Uh- oh, I think they're gonna fight!")
    if Person1.weight > Person2.weight and Person1.height > Person2.height:
        print("Oh snap!! They are fighting!!")
        print(Person1.name, "is bigger and taller than", Person2.name + ", so they had the advantage.")
        print("I blame you for this.")
        print("All you had to do was separate them!")
        print("You cannot stay here, bye!")
        exit()
    elif Person1.weight < Person2.weight and Person1.height < Person2.height:
        print("Oh my gosh! They're throwing hands!")
        print(Person2.name, "is killing", Person1.name + ".")
        print(Person1.name, "is dead.")
        print("This murder is on your hands!")
        exit()
    else:
        print("Wait.")
        print("I think they're getting along...")
        print("Hey, look at that.")
        if Person1.age < Person2.age:
            print("Awe,", Person2.name, "is taking care of", Person1)
            print("Good choice")
            exit()
        elif Person1.age > Person2.age:
            print("Hey would you look at that. Looks like they're playing cards.")
            print("They're friends now.")
            print("Good job")
            exit()

        elif Person1.age == Person2.age:
            rn = randint(-100, 100)
            if rn < 0:
                Warrior = Person("Warrior", 25, 72, 200, 100)
                print("Woah! Someone is coming!!")
                print('*Warrior has entered the chat*')
                print("Warrior: I'm gonna fight you!")
                if Warrior.strength > Person1.strength + Person2.strength and Warrior.weight > Person1.weight + Person2.weight and Warrior.height > Person1.height + Person2.height and Warrior.age > Person1.age + Person2.age:
                    print("And kill you!!")
                    print("\n\n\n\n\n")
                    print("           88                               88")
                    print("           88                         ,d    88")
                    print("           88                         88    88")
                    print(""" ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,""")
                    print("""a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a""")
                    print("""8b       88 8PP""""""" ,adPPPPP88   88    88       88""")
                    print(""" 8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88""")
                    print(""" `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88""")
                    print("\n\n\n\n\n")
                    print("You lose")
                    exit()

                elif Warrior.strength < Person1.strength + Person2.strength and Warrior.weight < Person1.weight + Person2.weight and Warrior.height < Person1.height + Person2.height and Warrior.age < Person1.age + Person2.age:
                    print("You stabbed the warrior... the warrior named ", Warrior.name)
                    print("You WiN")
                    exit()

                else:
                    print(Person1.name, "and", Person2.name, "the Warrior killed each other")
                    exit()

            elif rn > 0:
                Warrior = Person("Warrior", 40, 84, 300, 300)
                print("Woah! Someone is coming!!")
                print("*Warrior has entered the chat*")
                print("Warrior: My name is " + Warrior.name)
                print("         It makes no sense for you to try to fight me, but I will give a chance; 1/100th chance")
                input("PRESS ENTER TO DECIDE THEIR FATE")
                chance = randint(1, 100)
                if chance == 1:
                    print("Warrior: You actually defeated me...")
                    print("         You have survived, but not next time!")
                    print("You WiN")
                    exit()
                else:
                    print("\n\n\n\n\n")
                    print("           88                               88")
                    print("           88                         ,d    88")
                    print("           88                         88    88")
                    print(""" ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,""")
                    print("""a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a""")
                    print("""8b       88 8PP""""""" ,adPPPPP88   88    88       88""")
                    print(""" 8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88""")
                    print(""" `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88""")
                    print("\n\n\n\n\n")
                    print("You have been killed.")
                    exit()
            else:
                print("The Universe has been destroyed")
                print("Everyone loses")
                print("\n\n\n\n\n")
                print("           88                               88")
                print("           88                         ,d    88")
                print("           88                         88    88")
                print(""" ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,""")
                print("""a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a""")
                print("""8b       88 8PP""""""" ,adPPPPP88   88    88       88""")
                print(""" 8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88""")
                print(""" `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88""")
                print("\n\n\n\n\n")
                exit()
