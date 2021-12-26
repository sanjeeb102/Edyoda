#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class admin:
    food_item_list={1:{'Name' : 'Tandoori Chicken' , 'Quantity' : '4 piece' , 'Price' : 240 , 'Discount(%)' : 10 , "Stock" : 20}, 2:{'Name' : 'Vegan Burger ' , 'Quantity' : '1piece' , 'Price' : 320 , 'Discount(%)' : 5 , "Stock" : 15}, 3:{'Name' : 'Truffle Cake' , 'Quantity' : '500gms' , 'Price' : 900, 'Discount(%)' : 10, "Stock" : 10}}
    user_details = {}
    user_login=[]
    admin_details = {}
    count=3
    
    
    def __init__(self):
            print("Swad-Anusar-Food Ordering App")
    
    def admin_home(self):
        self.start_action = input("Press 1 for Admin Access \nPress 2 for User Access\n")
        if self.start_action == '1':
            self.ad_action = input('Press 1 >> Sign Up \nPress 2 >> Log in\n')
            if self.ad_action == '1':
                self.admin_signup()
            elif self.ad_action == '2':
                self.admin_log_in()
            else:
                print('Invalid Input')
                self.admin_home()
        elif self.start_action == '2':
            self.us_action = input('Press 1 >> Sign Up \nPress 2 >> Log in\n')
            if self.us_action == '1':
                self.user_signup()
            elif self.us_action == '2':
                self.user_login()
            else:
                print('Invalid Input')
                self.admin_home()
                    
    
# admin sign up for new admin    
    def admin_signup(self):
        print('Admin Sign Up')
        self.username = input("Enter Username:")
        self.password = input("Enter Password:")
        
        if self.username in admin.admin_details:
            print('Username already exists. Select a new one')
            self.admin_signup()
        else:
            admin.admin_details[self.username] = self.password
            print('New Admin Registered')
            self.admin_log_in()
    
# login for signed up admin with email and password    
    def admin_log_in(self):
        print("Admin Log in")
        self.username = input("Enter Username:")
        self.password = input("Enter Password:")
        
        if self.username in admin.admin_details:
            if self.password in admin.admin_details[self.username]:
                print('Login Successful')
                self.admin_login = True
                self.admin_main_menu()
            else:
                print('Wrong Password')
                self.admin_login = False
                self.admin_signup()
        else:
            print('Username not registered')
            self.admin_signup()
            self.admin_login = False
            
            
    def admin_main_menu(self):
        self.main_menu_action = input('Press 1 >> Add Food Item \nPress 2 >> Update Food Item Detail \nPress 3 >> View All Food Items \nPress 4 >> Remove Food Item \nPress 5 >> Admin Logout\n')
        if self.main_menu_action == '1':
            self.add_fooditem()
        elif self.main_menu_action == '2':
            self.edit_fooditem()
        elif self.main_menu_action == '3':
            self.all_fooditems()
        elif self.main_menu_action == '4':
            self.remove_fooditem()
        elif self.main_menu_action == '5':
            self.admin_logout()
            
# to add new food items in the lists of food items by admin    
    def add_fooditem(self):
        admin.count += 1
        self.food_id =  admin.count
        self.name = input("Item Name:")
        self.quantity = input("Quantity(in single serve):")
        self.price = input("Price:")
        self.discount = input("Discount(%):")
        self.stock = input("Stock Available:")
        
        try:
            if self.admin_login == True:
          
                admin.food_item_list[self.food_id] = {"Name" : self.name , 'Quantity' : self.quantity , 'Price' : self.price , 'Discount(%)' : self.discount , 'Stock' : self.stock}
                print(self.food_id,admin.food_item_list[self.food_id]['Name'],'successfully added to the menu')
                self.add_action = input('Press 0 >> Main Menu')
                if self.add_action == '0':
                    self.admin_main_menu()
                else:
                    print('Invalid input')
                    self.admin_home()
            
        except AttributeError:
            print('Admin login failed')
        except:
            print('Something Wrong')
            
    
# to edit specific details of food items already present in food item list    
    def edit_fooditem(self):
        self.food_id = int(input("Enter Food ID of Item you want to edit:"))
        try:
            if self.admin_login == True:
                if self.food_id in admin.food_item_list:
                    edit_action=input("Select from the options to edit:\nPress 1 >> Food Name\nPress 2 >> Quantity\nPress 3 >> Price\nPress 4 >> Discount\nPress 5 >> Stock \n")
                    if edit_action == '1':
                        input_name = input('Enter New Food Name:')
                        admin.food_item_list[self.food_id]["Food Name"] = input_name
                    elif edit_action == '2':
                        input_quantity = input('Enter New Quantity:')
                        admin.food_item_list[self.food_id]["Quantity"] = input_quantity
                    elif edit_action == '3':
                        input_price = int(input('Enter New Price:'))
                        admin.food_item_list[self.food_id]["Price"] = input_price
                    elif edit_action == '4':
                        input_discount = int(input('Enter New Discount:'))
                        admin.food_item_list[self.food_id]["Discount"] = input_discount
                    elif edit_action == '5':
                        input_stock = int(input('Enter New Stock'))
                        admin.food_item_list[self.food_id]["Stock"] = input_stock
                else:
                    print('Food ID does not match. Try Again.')
                    self.admin_main_menu()
                print('Detail of Food Item Updated.')
                print(admin.food_item_list[self.food_id]) 
                self.edit_action = input("Press 0 >> Main Menu\n")
                if self.edit_action == '0':
                    self.admin_main_menu()
                else:
                    print('Invalid input')
                    self.admin_home()
                
            
        except AttributeError:
            print('Admin login failed')
        except:
            print('Something Wrong')
    
    
# to view list of all food items present    
    def all_fooditems(self):
        try:
            if self.admin_login == True:
                print('List of items you are delivering:')
                for key in admin.food_item_list:
                     print(key,':',admin.food_item_list[key])                            
                
                
            self.all_action = input('Press 0 >> Main Menu')
            if self.all_action == '0':
                self.admin_main_menu()
            else:
                print('Invalid input')
                self.admin_home()
                
            
        except AttributeError:
            print('Admin login failed')
        except:
            print('Something Wrong in displaying all food items')
        
    
# to remove any specific food item with food id    
    def remove_fooditem(self):
        self.food_id = int(input("Enter Food ID of Item you want to remove:"))
        try:
            if self.admin_login == True:
                if self.food_id in admin.food_item_list:
                    
                    print('Deleting Food Item...')
                    time.sleep(1)
                    print(self.food_id,admin.food_item_list[self.food_id]['Name'],'deleted from the menu')
                    del admin.food_item_list[self.food_id]
                    self.admin_main_menu()
                    
                
                else:
                    print('No such FID found')
                    self.admin_main_menu()
                
            
        except AttributeError:
            print('Admin login failed')
#         except:
#             print('Something Wrong')
            
    
# to logout logged in admin    
    def admin_logout(self):
        try:
            if self.admin_login == True:
                self.admin_login = False
                print('logged out')
                self.admin_home()
        except AttributeError:
            print(" User not logged in")
    
       
# inherited class of user from admin
class user(admin):
  

    
    def __init__(self):
        print("Swad-Anusar - Order Food!")
        self.admin_home()

# to sign up new user            
    def user_signup(self):
        print("Lets get signed up!")
        self.name = input("Enter Full Name:")
        self.phone = input("Enter Phone Number:")
        self.email = input("Enter Email ID:")
        if self.email in admin.user_details:
            print("Email ID already Registered. Try Logging in")
            self.user_login()
        else:
            admin.user_details[self.email]={"Name":self.name,"Phone":self.phone}
            self.address = input("Enter Full Address:")
            self.password = input("Enter New Password:")
            self.prev_orders = [{"Name": None , "Quantity": None , "Price":0}]
            admin.user_details[self.email].update({"Address":self.address,"Password":self.password, "Previous Order": self.prev_orders})
            print("Details Submitted successfully. Login to Order Now!")
            self.user_login()
        
    
# to login signed up user with email id and password    
    def user_login(self):
        print("Login to Start Ordering!")
        self.email = input("Email ID:")
        self.password = input("Password:")
        if self.email in admin.user_details:
            if self.password in admin.user_details[self.email]["Password"]:
                print("Log in Successful")
                print("Lets get started.")
                admin.user_login.append(self.email)
                self.user_login = True
                print('*****')
                self.main_menu()
                    
            else: print("Password does not match")
        else: print('Incorrect Email ID ')
    
# to place new order/s from the list of given food items     
    def new_order(self):
        
        try:
            if self.user_login == True:
                print("We are delivering:")
                for key in admin.food_item_list:
                    
                    print(key , admin.food_item_list[key]["Name"] , admin.food_item_list[key]["Quantity"] , "INR", admin.food_item_list[key]["Price"] , sep="  ") 
                    
                self.order_action = list(map(int,input("\nEnter the Item Number/s you wish to add in your Bag: \n[For Example : 1,2] ").strip().split(',')))
                    
                
                print('Your Bag:')
                print("")
               
                for i in self.order_action:
                        print(i , admin.food_item_list[i]["Name"] , admin.food_item_list[i]["Quantity"] , 'INR', admin.food_item_list[i]["Price"] , sep="  ")
                        
                print('')
                print('Summary:')
                
               
            
        except AttributeError:
            print('User login failed. Log in again')
        except:
            print('Something Wrong')
            
    
# for updating the profile of logged in user    
    def update_profile(self):
        print('UPDATE USER PROFILE')
        try:
            if self.user_login == True:
        
                self.update_action = input('Press 1 >> Update Name \nPress 2 >> Update Phone Number \nPress 3 >> Update email \nPress 4 >> Update Address \nPress 5 >> Update Password \n')
                if self.update_action == '1':
                    self.new_name = input("Enter New Name:\n")
                    admin.user_details[self.email]["Name"] = self.new_name
                    print("Name Updated Successfully")
                    self.main_menu()

                if self.update_action == '2':
                    self.new_ph = input("Enter New Phone Number:\n")
                    admin.user_details[self.email]["Phone"] = self.new_ph
                    print("Phone Number Updated Successfully")
                    self.main_menu()

                if self.update_action == '3':
                    self.new_email = input('Enter New Email:\n')
                    if self.new_email == self.email:
                        print("New email cannot be same as existing email")
                        self.update_profile()
                    else:
                        admin.user_details[self.new_email] = admin.user_details.pop(self.email)
                        print("Email Updated Successfully")
                        self.main_menu()

                if self.update_action == '4':
                    self.new_address = input('Enter New Address:\n')
                    admin.user_details[self.email]["Address"] = self.new_address
                    print("Address Updated Successfully")
                    self.main_menu()

                if self.update_action == '5':    
                    self.new_password = input('Enter New Password:\n')
                    if self.new_password == self.password: 
                        print("New Password cannot be same as existing Password")
                        self.update_profile()
                    else:
                        admin.user_details[self.email]['Password'] = self.new_password
                        print("Password Changed Successfully")
                        self.main_menu()
                        
        except AttributeError:
            print('User login failed. Log in again')
        except:
            print('Something Wrong')

# view the option to place new order/ order history/ update profile to logged in user
         
    def main_menu(self):
        print('MAIN MENU')
        self.main_action = input("Press 1 >> Place New Order \nPress 2 >> Order History \nPress 3 >> Update Profile \nPress 0 >> Log Out\n")
        if self.main_action == "1":
            self.new_order()
        elif self.main_action == "2":
            self.order_history()
        elif self.main_action == "3":
            self.update_profile()
        elif self.main_action == '0':
            self.user_logout()
        else: 
            print(" Input does not match. Try again.")
            self.main_menu()
            

# to log out logged in user    
    def user_logout(self):
        self.user_login = False
        print('User logged out')
        self.admin_home()
    
admin=user()


# In[ ]:




