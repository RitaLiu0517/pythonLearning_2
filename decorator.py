# decorator 裝飾器
import time

def print_func(func):
    def inner():
        print('running' , func.__name__) #印出正在跑的func name
        func()
    return inner

def time_func(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('花費' , end - start , 'secs')
    return inner

@time_func #等同於第37行
@print_func #可疊加，等同於地35行
def test():
    for i in range(1000000):
        i += 1
    

# def test2():
#     print('hi')
    

# test()
# print("加工前")
# test = print_func(test) #test 是被decorator加工過再retun回來的的new test
# test()
# print("加工完成")

#有計時功能的decorator
# test = print_func(test) # 第18行爲此行的快寫
# test = time_func(test) #第19行爲此行的快寫


# test2 = print_func(test2)
# test2 = time_func(test2)
test()
# test2()