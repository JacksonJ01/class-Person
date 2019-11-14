# Jackson J.
# 11/13/19
# I will create the basis for a project I have had on my mind for a while


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = int(age)
        self.height = int(height)
        self.weight = int(weight)

    def person_des(self):
        print("Okay, we have", self.name)
        print(f"Hey, they're pretty young! Only {self.age} years old")
        print("Heh, and that's pretty short too,", self.height, "inches short")
        print("And would you look at that. A fat boi;", self.weight, "pounds heavy")


class Warrior(Person):

    def __init__(self, name, age, height, weight, strength):
        super().__init__(name, age, height, weight)
        self.strength = strength


name3 = input(">>>")
age3 = input(">>>")
height3 = input(">>>")
weight3 = input(">>>")

bob = Warrior(name3, age3, height3, weight3)
print(Warrior)
