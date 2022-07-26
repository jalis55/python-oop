import csv
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



Items.csv_data_reader()

print(Items.all_items)