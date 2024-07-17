def noerror(func):
        def result(n, d):
              if d == 0:
                    return 0
              else:
                    return func(n, d)
        return result
                    
       
@noerror
def divide(n,  d):
       return n  / d

print(divide(1,0))

