# main.py

from person import Customer , Admin
from restaurant import Restaurant
from food_item import FoodItem


pach_bhai = Restaurant('Pach Bhai Restaurant','pachbhai_official@gmail.com','zollarpar road , sylhet')
abir = Admin('Abir','abir@gmail.com','subidbazar,sylhet')
pach_bhai.add_admin(abir)



def admin_workflow() :

    while True :
        print('Enter your option : ')

        print('1.Add Item\n2.Remove Item\n3.Add Customer\n4.View Customers\n5.Remove Customer\n6.Update Price\n7.View Menu\n8.Exit')

        option = int(input('Your option is : '))

        if option==1 :

            item_name = input('Enter Item Name : ')
            item_quantity = int(input('Enter Quantity : '))
            item_price = int(input('Enter Unit Price : '))
            item = FoodItem(item_name,item_quantity,item_price)
            abir.insert_item(pach_bhai,item)

        elif option==2 :
            item_name = input('Enter the item name : ')
            abir.delete_item(pach_bhai,item_name)

        elif option==3 :

            customer_name = input('Enter Customer Name : ') 
            customer_email = input('Enter Customer Email : ')
            customer_address = input('Enter Customer Address : ') 
            customer = Customer(customer_name,customer_email,customer_address) 
            abir.insert_customer(pach_bhai,customer)

        elif option==4 :

            print('=> All Customers : ')
            abir.show_all_customers(pach_bhai) 

        elif option==5 :

            customer_email = input('Enter Customer Email ID : ')
            abir.remove_customer(pach_bhai,customer_email)

        elif option==6 :
            item_name = input('Enter Item Name : ')
            new_price = int(input('Enter Price : '))
            abir.update_price(pach_bhai,item_name,new_price) 

        elif option==7 :
            abir.show_full_restaurant_menu(pach_bhai)

        elif option==8 :
            break 
        else :
            print('Invalid Input')


def customer_workflow(customer) :

    while True :

        print('Enter your option : ')
        print('1.View Restaurant Menu\n2.Place Order\n3.Check Balance\n4.View Past Orders\n5.Add Balance\n6.Exit')

        option = int(input('Your option is : '))

        if option==1 :

            customer.view_restaurant_menu(pach_bhai)

        elif option==2 :
            item_name = input('Enter item name : ')
            item_quantity = int(input('Enter item quantity : '))
            msg = customer.place_order(pach_bhai,item_name,item_quantity)
            print(msg)

        elif option==3 :

            customer.check_balance()

        elif option==4 :

            customer.view_past_orders()

        elif option==5 :
            amount = int(input('Enter amount you need to add : '))
            customer.add_balance(amount)

        elif option==6 :

            break 

        else :

            print('Invalid Input')


while True :

    print('Enter your choice : ')
    print('1.Admin SignIn\n2.Customer SignIn\n3.Exit')
    choice = int(input('Enter your choice : '))

    if choice==1 :

        admin_email = input('Enter admin email : ')
        admin_found = 0 
        for admin in pach_bhai.admins :
            if admin.email==admin_email :
                print(f'Welcome {admin.name} in your account !!!')
                admin_found = 1 
                admin_workflow()
        if admin_found==0 :
            print('Invalid Email ID')
        admin_found = 0 
            
    elif choice==2:

        customer_email = input('Enter customer email : ')
        customer_found = 0 
        for customer in pach_bhai.customers :
            if customer.email == customer_email :
                print(f'Welcome {customer.name} in your account !!!')
                customer_found = 1 
                customer_workflow(customer)
        if customer_found==0 :
            print('Invalid Email') 

        customer_found = 0 

    elif choice==3:
        break 
    else :
        print('Please Enter Valid Choice')