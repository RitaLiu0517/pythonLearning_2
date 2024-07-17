import abc

class Animal(metaclass=abc.ABCMeta): #抽象類別內的方法不會被執行，因為他最終需要被override
    @abc.abstractmethod
    def make_sound(self):
        print("我怎樣都不會被執行")
        pass

class Cat(Animal):
    def make_sound(self): #override
        print("meow")

class Dog(Animal):
    def make_sound(self):
        print("bark")

class Person(Animal):
    def make_sound(self):
        print("hi")

c = Cat()
# c.make_sound()

d = Dog()
# d.make_sound()

p = Person()
# p.make_sound()

# 也可以用forloop去呼叫
for animal in [c,d,p]:
    animal.make_sound()
