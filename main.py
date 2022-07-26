
class Items:
    pay_rate=0.8 #discount rate 20%
    all_items=[]

    def __init__(self,name:str,price:float,qty=0) -> None:
        #preventing negative price and quantity
        assert price >=0,"Price can not be negative"
        assert qty >=0,"Quantity can not be negative"

        self.name=name
        self.price=price 
        self.qty=qty
        Items.all_items.append(self)

    def get_total_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        self.price=self.price * self.pay_rate
    def __repr__(self) -> str:
        return f"Items({self.name},{self.price},{self.qty})"

# item1=Items("phone",100,5)

# print(item1.name,item1.price,item1.qty)

# item2=Items("Laptop",1000,2)
# print(item2.name,item2.price,item2.qty)

#view attributes and methods of class and instances
# print(item1.__dict__)
# print(Items.__dict__)

# print(item1.get_total_price())
# item1.apply_discount()
# print(item1.get_total_price())

# item3=Items("mac",1000,1)
# item3.pay_rate=0.7
# item3.apply_discount()
# print(item3.get_total_price())

item1 = Items("Phone", 100, 1)
item2 = Items("Laptop", 1000, 3)
item3 = Items("Cable", 10, 5)
item4 = Items("Mouse", 50, 5)
item5 = Items("Keyboard", 75, 5)

print(Items.all_items)

item5.qty=item5.qty-1

print(Items.all_items)