import csv
class Items:
    pay_rate=0.8 #discount rate 20%
    all_items=[]

    def __init__(self,name:str,price:float,qty=0) -> None:
        #preventing negative price and quantity
        assert price >=0,"Price can not be negative"
        assert qty >=0,"Quantity can not be negative"

        self.__name=name
        self.price=price 
        self.qty=qty
        Items.all_items.append(self)

    #encapsulation..read-only name attribute
    @property
    #get name
    def name(self):
        return self.__name
    #set name
    @name.setter
    def name(self,value):
        self.__name=value

    def get_total_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        self.price=self.price * self.pay_rate

    @classmethod
    def csv_data_reader(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Items(
                name=item.get('name'),
                price=float(item.get('price')),
                qty=int(item.get('qty'))
            )

    def __repr__(self) -> str:
        return f"Items({self.name},{self.price},{self.qty})"



#encapsulation

items1=Items("Iphone",800,3)
print(items1.name)
items1.name='IphoneX'

print(items1.name)