# LEGB
# L: local    最小 最低層
# E: enclosed 包夾在function中間
# G: global   全域
# b: built-in 內建 最高層

y = 10      #global
x = 5       #global
def f():     #global
    x = 1   #enclosed
    def ff():
        x = 5   #local

def qwe():  #global
    q = 1   #local