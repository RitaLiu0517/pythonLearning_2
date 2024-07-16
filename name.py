# _
# _name
# name_ 為了避開相同命名
# __name
# __name__ python預留的function名

for _ in range(10): # _此處代表i的意思，也意指不重要以後用不到所以不用特意命名
    print(_ , "hi") 

name, _ = 'allan 18'.split(" ") #若age(18)再也用不到，也可用_代替


class Qwe:
    def public_function(self):
        print("public_function")
    
    def _private_function(self): #_在此代表此function是private，只能在同區域內使用 （Qwe()內使用）
        print('private_function')


# __name
class Person:
    def __init__(self):
        self.x = 1
        self._y = 1
        self.__z = 1 # 為了避免撞名，所以python的interpretor會把他自動重新命名

p = Person()
print(p.x)
print(p._y)
print(dir(p))
print(p.__z) #被重新改名為 '_Person__z'
        