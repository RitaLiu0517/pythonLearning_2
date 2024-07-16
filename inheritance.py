from dunder import Product #parent class / base class

#child class / derived class
class Drink(Product):  #()內寫要繼承的parent class的屬性

    #override 因為在child class 有init，所以不會執行parent的init
    def __init__(self, name, price, volume):
        super().__init__(name, price) #使用super可以取代下面兩行，使程式減少與父class的重複性
        # self.name = name
        # self.price = price
        self.volume = volume
    

d = Drink('珍珠奶茶', 80, 600)
print(d.volume)