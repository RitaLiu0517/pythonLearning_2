class Product:
    def __init__(self, name, price):
        self.name = name #property
        self.price = price #property
    
    def __str__(self):
        # return self.name + ' $' + str(self.price)
        return f'{self.name}  ${self.price}'
    print("珍珠奶茶", 60)

    def __repr__(self):
        return f'<Product({self.name}, {self.price})>'


    def __add__(self, other):
        if isinstance(other, str): #先檢查other是不是字串類型
            self.name += other
        if isinstance(other, Product): #先檢查other是不是Product
            return [self,other]
        
    def __mul__(self, other):
        result = []
        if isinstance(other, int):
            for _ in range(other):
                result.append(self)
        return result
    
p1 = Product('珍珠奶茶', 60)
p2 = Product('義大利麵', 220)
print(repr(p1))
p1 + '白玉'
print(p1)
print(p1 + p1)
print(p1 *5)
