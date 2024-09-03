# OOP: Write a Python class Person with attributes name and age, and a method greet that prints "Hello, my name is [name] and I am [age] years old.".
# Turtle: Write a Python script using the Turtle module to draw a square.
# Inheritance: Create a base class Vehicle with a method drive. Then, create a subclass Car that overrides the drive method to print "Car is driving".
# OOP & Inheritance: Create a class Animal with a method speak, and create two subclasses Dog and Cat that override the speak method to print "Woof" and "Meow", respectively.
# Turtle: Write a Python script using the Turtle module to draw an equilateral triangle

# _______________OOP__________________

class Person():
    def __init__(self) -> None:
        self.name='Abhi'
        self.age=18

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")    


person=Person()
person.greet()

# _______________turtle__________________

from turtle import Turtle,Screen

# turtle=Turtle()
screen=Screen()

# turtle.forward(100)
# turtle.setheading(90)
# turtle.forward(100)
# turtle.setheading(180)
# turtle.forward(100)
# turtle.setheading(270)
# turtle.forward(100)
# turtle.setheading(0)

# screen.exitonclick()


# _______________INHERITANCE__________________

class Vehicle():
    def __init__(self) -> None:
        self.drive()

    def drive(self):
        print("Car is driving")

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()

car=Car()

# _______________OOP & INHERITANCE__________________

class Animal():
     def __init__(self) -> None:
        self.speak()

    def speak(self):
        print('Speaking')

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.bark()

    def bark(self):
        print('Barking')

dog=Dog()

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.meow()

    def meow(self):
        print('Meow')

cat=Cat()

# _______________Turtle__________________

triangle=Turtle()

triangle.forward(100)
triangle.setheading(120)
triangle.forward(100)
triangle.setheading(240)
triangle.forward(100)


screen.exitonclick()



