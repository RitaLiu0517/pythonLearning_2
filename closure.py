# closure 閉包

def f():
    x = 1 
    def test():
        print('測試閉包有沒有被偷渡出來')

    class Test:
        def __init__(self):
            print('測試class有沒有一樣被偷渡出來')

    def inner():
        print(x)
        test()
        t = Test()
        
    return inner

result = f()
result()