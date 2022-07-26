class Items:
    def get_total_price(self,x,y):
        return x*y


item1=Items()
item1.name='phone'
item1.price=100
item1.qty=5

print(item1.get_total_price(item1.price,item1.qty))