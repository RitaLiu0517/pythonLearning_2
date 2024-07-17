# encapsulation 封裝
# oop
# private

class Batman:
    def __init__(self, hp) :
        self._hp = hp #加上＿代表private

    #getter method
    def get_hp(self):
        return self._hp
    
    #setter method 
    def set_hp(self, hp):
        self._hp = hp
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp 



b1 = Batman(100)
b2 = Batman(90)
#若b1的hp為b1+b2 ，寫法很麻煩如下：
b1.set_hp(b1.get_hp() + b2.get_hp())


#但其實python沒有private概念，_的表示只是約定俗成的信任，以下是python版的寫法
class Batman: 
    def __init__(self, hp) :
        self.hp = hp #property

#但是少了getter/setter，就無法在裡面新增條件，所以要使用 @property來裝飾
    @property  #python的getter
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
    
        if hp > 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp 
    


b1 = Batman(100)
b2 = Batman(90)
b1.hp = b1.hp + b2.hp