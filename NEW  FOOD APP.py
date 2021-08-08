#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class restraunt():
        list_of_admins={'username':'admin','password':'admin'}
        list_of_item=[]
        
        def admin():
            username=input('enter the username')
            password=input('enter the password')
            if (username in restraunt.list_of_admins['username']) and (password in restraunt.list_of_admins['password']):
                print("you logged in sucessfully")
            else:
                print("Please enter the correct data")
        def additem():
            import random
            name=input('enter the name of item')
            quantity=input('enter the quantity of item')
            price=input('enter the price of item')
            discount=input('enter the discount of item')
            stock=input('enter the stock present in restraunt')
            key=['foodid','name','quantity','price','discount','stock']
            values=[random.randint(1,9999),name,quantity,price,discount,stock]
            restraunt.list_of_item.append(dict(zip(key,values)))
            print('item is added sucessfully')
    
        def printitem():
            print(restraunt.list_of_item)
        def edititem():
                foodid=input('enter the food Id which you want to edit')
                for i in range(len(restraunt.list_of_item)):
                    restraunt.list_of_item[i]['foodid']==foodid
                    name=input('enter the name you want to edit')
                    restraunt.list_of_item[i]['name']=name
                    quantity=input('enter the quantity you want to edit')
                    restraunt.list_of_item[i]['quantity']=quantity
                    price=input('enter the price you want to edit')
                    restraunt.list_of_item[i]['price']=price
                    discount=input('enter the discount you want to edit')
                    restraunt.list_of_item[i]['discount']=discount
                    stock=input('enter the stock you want to edit')
                    restraunt.list_of_item[i]['stock']=stock
                    print('you edited item sucssfully')
                    break
        def deleteitem():
                 foodid=input('enter the food Id which you want to delete')
                 for i in range(len(restraunt.list_of_item)):
                    restraunt.list_of_item[i]['foodid']==foodid
                    del restraunt.list_of_item[i]
                    print('item is deleted sucessfully')
        def show_item():
            print('list of item')
            for i in range(len(restraunt.list_of_item)):
                print(restraunt.list_of_item[i]['foodid'],(restraunt.list_of_item[i]['quantity']),['INR'+"(restraunt.list_of_item[i]['price'])"])
class user:
    list_of_user=[]
    order=[]
    def user_registation():
        name=input('enter the full name')
        phone=input('enter the contact no.')
        address=input('enter the address')
        email=input('enter the email Id')
        password=input('enter the passwaord')
        key=['name','phone','address','email','password']
        values=[name,phone,address,email,password]
        user.list_of_user.append(dict(zip(key,values)))
        print('your registation is sucessful')
    def printuser():
        print(user.list_of_user)
    def user_login():
        email=input('enter the email Id')
        password=input ('enter the passwaord')
        for i in range(len(user.list_of_user)):
            if (user.list_of_user[i]['email']==email) and (user.list_of_user[i]['password']==password):
                print('you logged in sucessfully')
                return True
            else:
                print('you entered incorrect data')
                return False
    def edit_profile():
                 while user.user_login()==True:
                     
                        name=input('enter name to be edited')
                        user.list_of_user[i]['name']=name
                        phone=input('enter contact no. to be edited')
                        user.list_of_user[i]['phone']=phone
                        address=input('enter address to be edited')
                        user.list_of_user[i]['address']=address
                        email=input('enter email Id to be edited')
                        user.list_of_user[i]['email']=email
                        password=input('enter password to be edited')
                        user.list_of_user[i]['password']=password
                        print('profile is updated sucessfully')
                        
    def place_order():
        
        i = input("enter comma seprated the food ids: ")
        
        l = []
        l.append(i.split(','))
        print(l)
        user.order.append(l)
                 
    def order_history():
        print ('your order history',order)
                
                
if __name__ == '__main__':
    ans = True
    print("\nEnter the number corresponding to what you want to choose:")
    while ans:
            choice=int(input('/n1.for admin /n2.for borrower'))
            if choice==1:
                restraunt.admin()
                print('welcome admin')
                
                print("\nEnter the number corresponding to what you want to choose:")
                t=True
                while t:
                    choice=int(input('1.add item /n2.edit item /n3.list of item/n4.remove a item /n5.exit'))
                    if choice==1:
                        restraunt.additem()
                    elif choice==2:
                        restraunt.edititem()
                    elif choice==3:
                        restraunt.printitem()
                    elif choice==4:
                        restraunt.list_of_item()
                    else:
                        t=False
            elif choice==2:
                    print("\nEnter the number corresponding to what you want to choose:")
                
                    choice=int(input('1.register /n2.login'))
                    if choice==1:
                        user.user_registation()
                    elif choice==2:
                        user.user_login()
                        print('welcome user')
                        print("\nEnter the number corresponding to what you want to choose:")
                        i= int(input('1.update profile /n2.place order /n3.list of food/n4.exit'))
                        p=True
                        while p:
                            if i==1:
                                user.edit_profile()
                            elif i==2:
                                 user.place_order()
                            elif i==3:
                                restraunt.show_item()
                            else:
                                    p=False
                                     
                    else:
                        print('enter the correct choice')
            
                
                        


# In[ ]:




