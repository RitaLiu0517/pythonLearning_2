# generator 產生器
def g():
    while True:
        yield 1


def my_range(n):
    i = 0
    while i < n:
        print(f'我現在要給出{i}了')
        yield i
        i += 1
    
for i in my_range(5):
    print(i)

# list comprehension
x = [0, 1, 2, 3, 4]
print([i*i for i in x]) #是一個list，[]先裝好了

#generator expression 你需要他才給你
it = (i*i for i in x)
print(next(it))
print(next(it))

it1 = (i*i for i in x)
it2 = (i+2 for i in it1)
print(next(it2))
print(next(it2))