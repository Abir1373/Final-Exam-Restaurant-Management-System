# menu.py 

class Menu :

    def __init__(self):
        self.items = []

    def view_items(self) :
        print('*ItemName*' , '*ItemQuantity*', '*ItemPrice*')
        for item in self.items :
            print(item.item_name, item.item_quantity, item.item_price)

    def find_item(self,item_name) :
        for item in self.items :
            if item.item_name.lower() == item_name.lower() :
                return item 
        return None 

    def add_item(self,item) :
        print(f'=> {item.item_name} is added successfully !!!')
        self.items.append(item)

    def remove_item(self,item_name) :
        for item in self.items :
            if item.item_name.lower() == item_name.lower() :
                self.items.remove(item)
                return (f'=> {item_name} is deleted from the menu')
        return (f' = > {item_name} is not available')

    def update_price(self, item_name , amount) :
        for item in self.items :
            if item.item_name.lower() == item_name.lower() :
                item.item_price = amount 
                msg = f'{item_name} price update went successfully !!!!'
                return msg 
        return 'Item missing !!!!!'