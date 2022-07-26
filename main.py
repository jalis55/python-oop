from cgi import print_exception
from unicodedata import name


class Items:
    def __init__(self,name,price,qty) -> None:
        self.name=name
        self.price=price 
        self.qty=qty
    def get_total_price(self,x,y):
        return x*y


item1=Items("phone",100,5)

print(item1.name,item1.price,item1.qty)

