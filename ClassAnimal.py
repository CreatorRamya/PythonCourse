from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk, eat, talk, and run")

class Spider(Animal):

    def move(self):
        print("I can make webs.")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Spider()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
