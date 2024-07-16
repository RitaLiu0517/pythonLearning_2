# scope 範圍
# LEGB rule
# 低層不能改變高層的值
# 高層取不到低層的值

x = 1 #高層
def f():
    x = 10 #低層

f()
print(x) # x= 1