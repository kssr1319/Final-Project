# You have to design a Food Ordering app for a restaurant.
# The application will have a log-in for admin and users.

# Admin will have the following functionalities:
# Add new food items. Food Item will have the following details:
# FoodID //It should be generated automatically by the application.
# Name
# Quantity. For eg, 100ml, 250gm, 4pieces etc
# Price
# Discount
# Stock. Amount left in stock in the restaurant.
# Edit food items using FoodID.
# View the list of all food items.
# Remove a food item from the menu using FoodID.

# The user will have the following functionalities:
# Register on the application. Following to be entered for registration:
# Full Name
# Phone Number
# Email
# Address
# Password
# Log in to the application
# The user will see 3 options:
# Place New Order
# Order History
# Update Profile
# Place New Order: The user can place a new order at the restaurant.
# Show list of food. The list item should as follows:
# 1. Tandoori Chicken (4 pieces) [INR 240]
# 2. Vegan Burger (1 Piece) [INR 320]
# 3. Truffle Cake (500gm) [INR 900]
# Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]
# Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
# Order History should show a list of all the previous orders
# Update Profile: the user should be able to update their profile.

def login(id,password):
    if(id == "200303" and password == "1308sand"):
        print("admin sandeep has logged in" )
    else:
        print("Invalid id or password")
def register(name,password):
    print("successfully registered")
def access(option):
    if(option == "login"):
        id = input("Enter your admin login ID: ")
        password = input("Enter your admin password: ")
        login(id,password)
    else:
        print("Enter your Name and Password to register as user")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)
def foodapp():
    global option
    print("Welcome to Edyoda Food ordering app")
    option = input("login or register (login,reg): ")
    if(option!="login" and option!="reg"):
        foodapp()
foodapp()
access(option)
class food:

    def __init__(self,food_id,food_name,food_quantity,food_price,food_discount,food_stock):
        self.food_id = food_id
        self.food_name = food_name
        self.food_quantity = food_quantity
        self.food_price = food_price
        self.food_discount = food_discount
        self.food_stock = food_stock

    def __str__(self):
        return f"food ID : {self.food_id} \nfood Name : {self.food_name} \nfood quantity : {self.food_quantity} \nfood Price : {self.food_price} \nfood discount : {self.food_discount} \nfood stock : {self.food_stock}"

    def set_food_id(self,food_id):
        self.food_id = food_id

    def get_food_id(self):
        return self.food_id

    def set_food_name(self,food_name):
        self.food_name = food_name

    def get_food_name(self):
        return self.food_name
            
    def set_food_quantity(self,food_quantity):
        self.food_quantity = food_quantity

    def get_food_quantity(self):
        return self.food_quantity

    def set_food_price(self,food_price):
        self.food_price = food_price

    def get_food_price(self):
        return self.food_price
    
    def set_food_discount(self,food_discount):
        self.food_discount = food_discount

    def get_food_discount(self):
        return self.food_discount
    
    def set_food_stock(self,food_stock):
        self.food_stock = food_stock

    def get_food_stock(self):
        return self.food_stock

class menuoption:
    menu = []
    def add_menu(self):
        Food_id = int(input("Enter food Id : "))
        Food_name = input("Enter food Name : ")
        Food_quantity = input("Enter food quantity : ")
        Food_price = float(input("Enter food Price : "))
        Food_discount = float(input("Enter discount Price: "))
        Food_stock = float(input("Enter the items quantity left in stock: "))
        Food_obj = food(Food_id,Food_name,Food_quantity,Food_price,Food_discount,Food_stock)
        self.menu.append(Food_obj)
        print("New menu Successfully Added!")

    def view_menu(self):
        for i in self.menu:
            print()
            print(i)

    def delete_menu(self):
        Food_id = int(input("Enter item id in menu you want to delete : "))
        for foods in self.menu:
            if foods.Food_id == Food_id:
                self.menu.remove(foods)
                print("Successfully Deleted item from menu")
                break
        else:
            print("No item Found!")

class menu:

    def __init__(self,menuoption_obj):
        self.menuoption_obj = menuoption_obj

    def execute(self,choice):
        if choice == 1:
            print("***********Add Food Item***********")
            self.menuoption_obj.add_menu()

        elif choice == 2:
            print("***********View Menu**********")
            self.menuoption_obj.view_menu()

        elif choice == 3:
            print("***********Delete Food Item**********")
            self.menuoption_obj.delete_menu()

        else:
            print("Invalid Choice")

if __name__ == "__main__":
        menuoption_obj = menuoption()
        menu = menu(menuoption_obj)
        while True:
            print("Enter \n1.Add Food Item \n2.View Menu \n3.Delete Food Item")
            choice = int(input("Enter your choice : "))
            menu.execute(choice)

class User:
    def _init_(self,user_id,user_name,phone_number,Email,Address,password):
        self.user_id = user_id
        self.user_name = user_name
        self.phone_number = phone_number
        self.Email = Email
        self.Address = Address
        self.password = password
    def _str_(self):
        return f"User ID : {self.user_id} \nUser Name : {self.user_name} \nPhone Number : {self.phone_number} \nEmail : {self.Email} \nAddress : {self.Address}"
    def set_user_id(self,user_id):
        self.user_id = user_id
    def get_book_id(self):
        return self.user_id
    def set_user_name(self,user_name):
        self.user_name = user_name
    def get_book_name(self):
        return self.user_name
    def set_phone_number(self,phone_number):
        self.phone_number = phone_number
    def get_phone_number(self):
        return self.phone_number
    def set_Email(self,Email):
        self.Email = Email
    def get_Email(self):
        return self.Email
    def set_Address(self,Address):
        self.Address = Address
    def get_Address(self):
        return self.Address
class userreg:
    user = []
    def add_user(self):
        user_id = input("Enter User id:" )
        user_name = input("Enter User Full Name: ")
        phone_number = int(input("Enter Phone Number: "))
        Email = input("Enter E-mail: ")
        Address = input("Enter Address: ")
        password = input("Enter Password: ")
        user_obj = User(user_id,user_name,phone_number,Email,Address,password)
        self.user.append(user_obj)
        print("User Successfully Registered!")
    def view_user(self):
        for i in self.user:
            print()
            print(i)
    def update_user(self):
        user_id = input("Enter User Id of the user you want to update : ")
        for Users in self.user:
            if Users.user_id == user_id:
                user_name = input("Enter User Full Name: ")
                phone_number = int(input("Enter Phone Number: "))
                Email = input("Enter E-mail: ")
                Address = input("Enter Address: ")
                password = input("Enter Password: ")
                Users.set_book_name(user_name)
                Users.set_book_edition(phone_number)
                Users.set_book_author(Email)
                Users.set_book_publisher(Address)
                Users.set_book_price(password)
                print("Successfully Updated User")
                break
        else:
            print("No User Found!")
class UserMain:
    def _init_(self,userfunction_obj):
        self.userfunction_obj = userfunction_obj
    def execute(self,ch):
        if ch == 1:
            print("Add User")
            self.userfunction_obj.add_user()
        elif ch == 2:
            print("View User")
            self.userfunction_obj.view_user()
        elif ch == 3:
            print("Update User")
            self.userfunction_obj.update_user()
        else:
            print("Invalid Choice")
if __name__ == "_main_":
    userfunction_obj = userreg()
    usermain = UserMain(userfunction_obj)
    while True:
        print("Enter \n1.Add user \n2.View user \n3.Update user")
        ch = float(input("Enter your choice : "))
        usermain.execute(ch)
