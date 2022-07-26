
class Items:
    def __init__(self,name,price,qty=0) -> None:
        self.name=name
        self.price=price 
        self.qty=qty
    def get_total_price(self,x,y):
        return x*y


item1=Items("phone",100,5)

print(item1.name,item1.price,item1.qty)

item2=Items("Laptop",1000)
print(item2.name,item2.price,item2.qty)
