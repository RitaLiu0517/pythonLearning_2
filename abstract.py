# abstract class 抽象類別
from abc import ABCMeta, abstractmethod #abstract base class

# class Product(): #base type
class Product(metaclass=ABCMeta):
    @abstractmethod
    def hi(self):
        pass

class Drink(Product):
    def hi(self): #override
        print ('hi')

# p = Product() #instance 實例
d = Drink()