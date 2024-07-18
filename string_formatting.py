x = 5  # 程式後面空兩格，#號後面空一格 

# docstring  # doc documentation  介紹module 或是 class 的註解（說明書）

class Batman:

    """_summary_
    kj;fafl;j
    fkaj;f

    """


# string Formatting
    
# pringf 舊型
name = 'Allen'
x = 5
y = 3.14
# print('hi %s' % name) # 字串型用s   # hi Allen
# print('hi %d' % x) # 整數用d   # hi 5
# print('hi %f' % y) # 小數用d   # hi 3.140000
# print('hi %s, my number is %d' % (name, x) ) # 組合 # hi Allen, my number is 5


# 新型
# print('hi {}, my number is {}'.format(name, x))

#python3.6之後才有的
print(f'hi {name}, my number is {x}')
print(f'hi {name:>10}, my number is {x}') # 往右對齊10個字元 # hi      Allen, my number is 5
print(f'hi {name:<10}, my number is {x}') # 往左對齊10個字元 # hi Allen     , my number is 5


