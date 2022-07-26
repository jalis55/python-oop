
class Items:
    pay_rate=0.8
    def __init__(self,name:str,price:float,qty=0) -> None:
        #preventing negative price and quantity
        assert price >=0,"Price can not be negative"
        assert qty >=0,"Quantity can not be negative"


        self.name=name
        self.price=price 
        self.qty=qty

        

    def get_total_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        self.price=self.price * Items.pay_rate


item1=Items("phone",100,5)

print(item1.name,item1.price,item1.qty)

item2=Items("Laptop",1000,2)
print(item2.name,item2.price,item2.qty)

#view attributes and methods of class and instances
# print(item1.__dict__)
# print(Items.__dict__)

print(item1.get_total_price())
item1.apply_discount()
print(item1.get_total_price())

