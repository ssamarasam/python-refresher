class Animal:
    def __init__(self):
        print("animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):

        print("mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)
print(m.weight)
