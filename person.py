#person.py

from abc import ABC 
from food_item import FoodItem

class Person(ABC) :

    def __init__(self,name,email,address):
        
        self.name = name 
        self.email = email 
        self.address = address
        self.balance = 10000 
        self.past_orders = []
    
class Customer(Person) :

    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    
    def view_restaurant_menu(self,restaurant) :
        restaurant.menu.view_items()

    def place_order(self,restaurant,item_name,item_quantity) :
        item = restaurant.menu.find_item(item_name) 
        required_money = item_quantity * item.item_price 
        if required_money <= self.balance and item.item_quantity>=item_quantity :
            for itm in restaurant.menu.items :
                if itm==item :
                    itm.item_quantity = itm.item_quantity - item_quantity
                    self.balance = self.balance - required_money
                    self.past_orders.append(FoodItem(itm.item_name,item_quantity,itm.item_price))
                    return 'order placed successfully !!!'
        return '### Order can not be placed ###'
        


    def check_balance(self) :
        print(f'Current Balance : {self.balance}')

    def view_past_orders(self) :
        print('Item Name /  Item Quantity  / Unit Price')
        for item in self.past_orders :
            print(item.item_name,item.item_quantity,item.item_price)

    def add_balance(self,amount) :
        self.balance += amount 
        return '{amount} added successfully'

class Admin(Person) :
        
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def insert_item(self,restaurant,item) :
        restaurant.menu.add_item(item)

    def delete_item(self,restaurant,item_name) :
        msg = restaurant.menu.remove_item(item_name)
        print(msg)

    def update_price(self,restaurant,item_name,new_price) :
        msg = restaurant.menu.update_price(item_name,new_price)
        print(msg)
    
    def insert_customer(self,restaurant,customer) :
        restaurant.add_customer(customer) 

    def show_all_customers(self,restaurant) :
        restaurant.view_customers()

    def remove_customer(self,restaurant,customer_email) :
        msg = restaurant.delete_customer(customer_email)
        print(msg)

    def show_full_restaurant_menu(self,restaurant) :
        restaurant.menu.view_items()