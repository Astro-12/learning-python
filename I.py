'''
What is Inheritance:
  -Inheritance is a key concept of oop
  -with inheritance a child class can use the attributes and methods of a base or parent class.
  -allows you to reuse your code, create clear hierarchies, and customize behavior without rewriting everything.

How to implement inheritance:
'''
  class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

  class Dog(Animal):
      bark = 'woof! woof!! woof!!!'
  
  jack = Dog('Jack')
  print(jack.sound())  # Jack makes a sound
  print(jack.bark)  # woof! woof!! woof!!!
