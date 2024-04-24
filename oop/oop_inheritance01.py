class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)

f = Fish()
f.swim()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
o = object()
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, Mammal))
