# Jackson J.
# 11/13/19
# I will create the basis for a project I have had on my mind for a while


class Person:
    def __init__(self, name, age, height, weight, strength):
        self.name = name
        self.age = int(age)
        self.height = int(height)
        self.weight = int(weight)
        self.strength = int(strength)

    def person_des(self):
        print("Okay, we have", self.name)
        print(f"Hey, they're pretty young! Only {self.age} years old")
        print("Heh, and that's pretty short too,", self.height, "inches short")
        print("And would you look at that. A fat boi;", self.weight, "pounds heavy")
