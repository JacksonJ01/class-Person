# Jackson J.
# 11/13/19
# I will create the basis for a project I have had on my mind for a while
from classPerson import Person
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

Person1 = Person(name, age, height, weight)

input("PRESS ENTER TO ENTER THOSE VALUES")
Person1.person_des()

print("\nNow for the second person. What will their attributes be")
print("Name:")
name2 = input(">>>").title()
print("Age:")
age2 = input(">>>")
print("Weight:")
weight2 = input(">>>")
print("And the Height:")
height2 = input(">>>")

Person2 = Person(name2, age2, height2, weight2)

print(f"\nSo we have {Person1.name} and {Person2.name}")
if separate == "Separate" or separate == "Se":
    print("Hm, they seem lonely. You decided to separate them. They could have started a civilation.")
    print("At least they aren't able to fight each other. That's good")

elif separate == "Socialize" or separate == "So":
    print("Uh- oh, I think they're gonna fight!")
    if Person1.weight and Person1.height > Person2.weight and Person2.height:
        print("Oh snap!! They are fighting!!")
        print(Person1.name, "is bigger and taller than", Person2.name + ", so they had the advantage.")
        print("I blame you for this.")
        print("All you had to do was separate them!")
        print("You cannot stay here, bye!")
        exit()
    elif Person1.weight and Person1.height < Person2.weight and Person2.height:
        print("Oh my gosh! They're throwing hands!")
        print(Person2.name, "is killing", Person1.name)
        print(Person1.name, "is dead.")
    else:
        print("I think they got along..")
        print("Hey, look at that.")
        if Person1.age < Person2.age:
            print()
        elif Person1.age > Person2.age:
            print()

