# @staticmethod
# @classmethod

class Batman:
    def __init__(self, hp):
        self.hp = hp

    def f(self): 
        print('就算沒有self，也呼叫到囉')

    @staticmethod #不需創作實例就可以使用的裝飾器
    def calc_avg(x):
        return sum(x) / len(x)
        f() #但這樣我就呼叫不到同class裡的f()，所以有了 @classmethod ：
    
    @classmethod
    def noself(cls):
        cls(100).f() #先假裝創作實例，並帶入參數，這樣就可以使用同class裡的method

# Batman.f()
# x = [1, 2, 3]
# print(Batman.calc_avg(x)) #不需實例就可調用
Batman.noself()