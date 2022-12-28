import re
#************************************Admin********************************************
class Restaurent:
    
    def __init__(self):
        self.Restaurent_name={}
        self.food={}
        self.food_ID=len(self.food)+1
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]

    def admin_registration(self):
            self.Restaurent_name = input("Enter Restaurent Name: ")
            self.email = input("Enter your email id : ")
            self.password = input("Enter your password : ")
            self.admin_details = {"Email_ID":self.email,"Password":self.password}
            print("\n\U0001f44d Restaurent Account is Created Successfully \U0001f44d\n")
            print(f"Welcome TO {self.Restaurent_name} Restaurant\n")
            print("Entered Admin Details : ")
            with open("D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Tharun Python\\Edyoda\\Final_Project\\Admin.txt","a+") as file:
                file.write("\n Restaurent Name: "+str(self.Restaurent_name))
                file.write("\n Admin Login details: "+str(self.admin_details))
            for i in self.admin_details:
                print(i, ":", self.admin_details[i])

    def admin_login(self):

        print(f"\nEnter {self.Restaurent_name} Restaurent login details \n")
        email = input("Enter Your Email ID : ")
        password = input("Enter Your Password : ")
        if len(self.admin_details.values())!=0:
            if email == self.email and password == self.password:
                print("\n \U0001F603 Logined successfully \U0001F603")
                while True:
                    print("1. Add Food Items \n2. View Food Items \n3. Edit Food Items \n4. Delete Food Items \n5. Quit Admin Page")
                    Inpt =input("Enter Here : ")
                    if Inpt == "1":
                        self.add_food_items()
                    elif Inpt == "2":
                        self.view_food_items()
                    elif Inpt == "3":
                        self.edit_food_items()
                    elif Inpt == "4":
                        self.delete_food_items()
                    elif Inpt == "5":
                        break
                    else:
                        print("invalid Input")
            else:
                print("\n\U0001F629 Incorrect Email or Password \U0001F629\n")
        else:
            print("\n<Admin account details not found>\n<Please enter correct details>\n")

    def add_food_items(self):

        name=input("Enter the food name : ")
        quantity=float(input("Enter the quantity in grams only : "))
        price=float(input("Enter the price in rupees only : "))
        discount=float(input("Enter the discount in rupees only : "))
        stock=int(input("Enter the available stock : "))
        food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
        self.food_ID=len(self.food)+1
        self.food[self.food_ID]=food_item
        with open("D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Tharun Python\\Edyoda\\Final_Project\\Admin.txt","a+") as file:
            file.write("\nfood items: "+str(self.food))
            file.truncate()
            print("\n\U0001F603 Food Item added successfully \U0001F603\n")
            print("Newly Added items :",self.food,"\n")

    def view_food_items(self):

        print("Food Items List : \n")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("\U0001F629 !!SORRY!! No Items found \U0001F629\n")

    def edit_food_items(self):

        edit = int(input("Enter the Food ID to update : \n"))
        if edit in self.food.keys():
            print("1. Update Food Name \n2. Update Quantity \n3. Update Price \n4. Update Discount \n5. Update Stock \n")
            edit_items = input("Enter only numbers as mentioned : ")
            if edit_items == "1":
                self.food[edit]["Name"] = input("Update the Food name : ")
                print("\n\U0001F603 Successfully Updated \U0001F603\n")
            elif edit_items == "2":
                self.food[edit]["Quantity"] = float(input("Update the Quantity in grams only : "))
                print("\n\U0001F603 Successfully Updated \U0001F603\n")
            elif edit_items == "3":
                self.food[edit]["Price"] = float(input("Update the Price in ripees only : "))
                print("\n\U0001F603 Successfully Updated \U0001F603\n")
            elif edit_items == "4":
                self.food[edit]["Discount"] = float(input("Update the Price in Rs only : "))
                print("\n\U0001F603 successfully Updated \U0001F603\n")
            elif edit_items == "5":
                self.food[edit]["Stock"] = int(input("Update the Stock : "))
                print("\n\U0001F603 Successfully Updated \U0001F603\n")
            else:
                print("\U0001F629 Sorry Invalid Number \U0001F629\n")
        else:
            print("\n<<< Incorrect Food ID >>>\n")

    def delete_food_items(self):

        print("\U0001f44e Warning \U0001f44e \nFood Item will be deleted Permanently\n")
        print("Enter the Food ID ")
        delt = int(input("Enter Here : "))
        if delt in self.food.keys():
            del self.food[delt]
            print("\n\U0001f44e Food item deleted successfully \U0001f44e\n")
            print("Updated Food List is: \n",self.food)
        else:
            print("<<< Incorrect Food ID >>>\n")

#*******************************User************************************************************

    def user_register(self):

        user_name=input("Enter your full name : ")
        phone_no=re.findall(r"^[1-9]{1}[0-9]{9}$",(input("Enter your 10 digit phone number : ")))
        email=input("Enter your Email ID : ")
        password=input("Enter your password : ")
        address=input("Enter your address with area PIN code : ")
        self.user_details={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
        print("\n\U0001f44d Your Account is Created Successfully \U0001f44d\n")
        print("Entered Details are : ")
        for i in self.user_details:
            print(i, ":", self.user_details[i])        

    def user_login(self):

        print("\nFor login Enter Email ID and Password\n")
        email = input("Email ID : ")
        password = input("Password : ")
        if len(self.user_details.values())!=0:                                                            #we can same as admin by using self.email..etc
            if email == self.user_details["Email_ID"] and password == self.user_details["Password"]:      # we can make it either object level or local level inside def fun
                print("\n\U0001F603 Logined successfully \U0001F603")
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Quit Login page")
                    options = input("Enter Here : ")
                    if options=="1":
                        self.place_order()
                    elif options=="2":
                        self.ordered_history()
                    elif options=="3":
                        self.update_details()
                    elif options=="4":
                        break
                    else:
                        print("invalid Number")
            else:
                print("\n\U0001F629 Incorrect Email or Password \U0001F629\n")
        else:
            print("\n!<<<There is no User Account with this Email ID !\n\n!! Please Creat Your Account First>>>!\n")

    def place_order(self):

        print("\nWelcome to Restaurant\n")
        print("\nEnter 1 to See Food Items")
        options = input("Enter here : ")
        if options == "1":
            print(f"\n Available Food is: {self.food}")
            print("\nEnter options based on Food ID")
            enter = int(input("Enter Here : "))
            if enter == self.food_ID:
                print("\n\U0001F603 Successfully Ordered \U0001F603")
                history = self.food[enter]
                self.ordered_item.append(history)
                print("Selected food item is : ", history)
            else:
                print("?? Entered option is incorrect ??")
        else:
            print("<<< Invalid Number >>>\n")

    def ordered_history(self):

        print("\nList of Previous ordered : \n")
        for order in self.ordered_item:
            print(order)

    def update_details(self):

        while True:
            print("To update profile enter below options\n")
            print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Quit\n")
            options = input()
            if options == "1":
                self.user_details["User Name"]=input("Enter your name to updat : ")
                print("\n\U0001F603 Details Updated Successfully \U0001F603\n")
            elif options == "2":
                self.user_details["Phone No."]=int(input("Enter phone number to update: "))
                print("\n\U0001F603 Detail Updated Successfully \U0001F603\n")      
            elif options == "3":
                self.user_details["Email_ID"]=input("Enter email id to update : ")
                print("\n\U0001F603 Detail Updated Successfully \U0001F603")
                
            elif options == "4":
                self.user_details["Password"]=input("Enter new password to update : ")
                print("\n\U0001F603 Detail Updated Successfully \U0001F603\n")
                
            elif options == "5":
                self.user_details["Address"]=input("Enter new address to update : ")
                print("\n\U0001F603 Detail Updated Successfully \U0001F603\n")
            
            elif options=="6":
                break
            else:
                print("\n\U0001F629 Invalid Number Entered \U0001F629\n")
                
            if options in ["1","2","3",'4',"5"]:
                for i in self.user_details:
                    print(i, ":",self.user_details[i])
            else:
                print("\n<<< Please Enter correct Input >>>\n")      


def Main():

    while True:
        print("\n***********************************!-FOOD IS GOOD-!***********************************")
        print("\U0001F609 Welcome \U0001F609")
        print(("Enter:\n 1. ADMIN\n 2. USER\n 3. Quit"))
        enter = input("Enter Here : ")
        if enter == "1":
            while True:
                print("***********************************ADMIN PAGE***********************************")
                print("\n\U0001f44d  Hello Admin  \U0001f44d")
                print("\nEnter following options to proceed\n")
                print("1. Admin Register\n2. Admin Login\n3. Quit Application\n")
                
                ent1 = input("Enter Here : ")
                if ent1 == "1":
                    obj = Restaurent()
                    obj.admin_registration()
                elif ent1 == "2":
                    obj.admin_login()           
                elif ent1 == "3":
                        break
                else:
                    print("\n Invalid Number ")
                    
        elif enter == "2":
            while True:
                print("***********************************USER PAGE***********************************")
                print("\n\U0001f44d  Hello User  \U0001f44d")
                print("\nEnter below options to proceed\n")
                print("1. User Register\n2. User Login\n3. Quit Application")
                ent2 = input("\nEnter Here : ")
                if ent2 == "1":
                    obj.user_register()
                elif ent2 == "2":
                    obj.user_login()           
                elif ent2 == "3":
                    break
                else:
                    print("\n Invalid Number ")        
        elif enter == "3":
                break
        else:
            print("\n Invalid Input ")

if __name__ == "__main__":
    Main()

