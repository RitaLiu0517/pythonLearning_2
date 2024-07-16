# pass by value  #複製本尊給分身，不會直接改變function外的x值 x = [0]
# pass by reference #本尊直接投入，會直接改變function外的x值 x = [0,1]

def f(y):
    y.append(1)

x = [0]
f(x)
print(x) #[0,1]


def ff(y):
    y += 1

x = 0 
# x = 'Allen' 
ff(x)
print(x)  # x = 0 
# print(x)  # x = 'Allen'

# 總結：python 的模式是 pass by object reference
# 只要物件被重新指向 “＝” ，原值就不會被改變

def f(y):
    y.append(1) #沒有等號，沒有被重新指向，x原值改變

x = [0]
f(x)
print(x) #[0,1]

def f(y):
    y = [] # 有等號，y重新指向，x原值不改變

x = [0]
f(x)
print(x) #[0]