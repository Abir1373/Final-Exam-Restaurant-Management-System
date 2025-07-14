#restaurant.py

from menu import Menu 

class Restaurant :

    def __init__(self,name,email,address):
        self.name = name 
        self.address = address 
        self.email = email 
        self.customers = [] 
        self.admins = []
        self.menu = Menu()

    def check_customer_info(self,customer_email) :
        for customer in self.customers :
            if customer.email == customer_email :
                return customer 
        return None 


    def add_customer(self,customer) :
        print(f'{customer.name} is added successfully')
        self.customers.append(customer)
    
    def add_admin(self,admin) :
        print(f'{admin.name} is added successfully')
        self.admins.append(admin)

    def view_customers(self) :
        print('*All Customers Info*')
        for customer in self.customers :
            print(customer.name, customer.email,customer.address)

    def delete_customer(self,customer_email) :
        for customer in self.customers :
            if customer.email==customer_email :
                self.customers.remove(customer) 
                return ('=> Customer id is deleted successfully')
        return '=> ID can not be deleted' 