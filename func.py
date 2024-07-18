# enumerate
x = ['a', 'b', 'c', 'd']

for i, name in enumerate(x):
    print(i , name)



# lambda : 匿名函式，通常使用在一次性 function 快寫法
def f(x):
    return x + 1

a = lambda x: x + 1
print(a(1))

products = [
    ('巧克力可可碎片', 145),
    ('香草可可碎片', 125),
    ('香蕉奶昔可可碎片', 155),
]
# 使用價格排序時就可以用到lambda
print(sorted(products, key=lambda x: x[1]))

p0 = {
    'name': '麥當勞',
    'price': 155,
}

p1 = {
    'name': '肯德基',
    'price': 105,
}

p2 = {
    'name': '頂呱呱',
    'price': 99,
}
products = [p0, p1, p2]
print(sorted(products, key=lambda x: x['price']))



# map
x = ['qazxsw', 'ecvfrtgbn', 'ertyuiopffgg']
print(list(map(len, x))) # 印出清單的長度，再存回清單內

for i in map(len,x) : # 沒存回清單的樣式 
    print(i)

#map 搭配 lambda
x = [1, 2, 3, 4]
print(list(map(lambda i: i * i , x ))) # [1, 4, 9, 16]
# list(map(lambda i: i * i , x )) 又等於：
print(i * i for i in x) # [1, 4, 9, 16]



# filter
print(list(filter(lambda i : i < 3, x))) # [1, 2] # 也等於： 
print([i for i in x if i < 3]) # [1, 2]
# 一般function表示法
def f(x):
    if x > 2:
        return False
    else:
        return True
print(list(filter(f, x))) # [1, 2]



#zip 組合
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a,b))) #[(1, 4), (2, 5), (3, 6)]