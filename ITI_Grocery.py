import time
import csv
from prettytable import PrettyTable
goods={
"list": ["apple","banana","cherry","mango"],
"prices":[10	,	8	,	25	,	18],
"stocks":[25	,	40	,	10	,	20],
}
customer=1
owner=1
count=0
pwd='Passw0rd@123.'
list1=[]
list2=[]
list3=[]
listprice=[]
listtotal=[]
x=1
while(x):
	buying_list=[]
	buying_price=[]
	buying_amount=[]
	listprice=[]
	total=0
	print("------------ Welcome to ITI Grocery Shop ------------")
	mode=input("(1)Customers \n(2)the Owner \n(0)Exit\n")		#Entering either customer mode or owner's mode(password required for owner)
	print("-----------------------------------------------")
	if mode=='2':
		owner=1
		while(owner):
			password=input("Enter the password : ")				#enter password :) *hint* Passw0rd@123.
			if (password==pwd):
				owner=int(input("(1)Show Products \n(2)Add Products \n(3)Change Cost \n(0)Exit\n"))	
				if owner==1:
					print("-----------------------------------------------")
					print(goods.items())						#show a list of products being sold 
					print("-----------------------------------------------")
					
				elif owner==2:
					print("-----------------------------------------------")
					product=input("Enter Product Name : ")			#to add new products
					product=product.lower()
					goods["list"].append(product)
					price=int(input("Enter the product price : "))
					goods["prices"].append(price)
					stock=int(input("Enter the Amount : "))
					goods["stocks"].append(stock)
					print("-----------------------------------------------")
				elif owner==3:
					print("-----------------------------------------------")
					e=int(input("Which element u want to change its price : "))			#Change the cost value of a current product already entered.
					price=int(input("Enter the new product's price : "))
					p=e-1
					goods["prices"].pop(p)
					goods["prices"].insert(p,price)
					print("-----------------------------------------------")
				elif owner==0:															#Exit of owner's mode to main menu.
					print("-----------------------------------------------")
					owner=0
					print("Exiting Owner's Mode")
					print("-----------------------------------------------")
					break;
				else:
					print("-----------------------------------------------")			#Wrong Input m8 check ur self again.
					print("Wrong Entry , Try again.")
					print("-----------------------------------------------")
			elif(count==3):																#BYE MASTER!!
				owner=0
				break;
			else:
				print("invalid Password.")												#1)Wrong password buddy ;) can't let you pass
				count+=1																#2)you good mate? dont u remember me?
				if (count==3):																	
					count=0																#3)since i am not important to u anymore... i am breaking up with you.
					break;																
	elif mode=='1':
		customer=1
		while(customer):
			customer=int(input("(1)Buy\n(2)Show Buying list\n(3)Print Bill\n(0)Exit\n"))
			if customer==1:
				print("-----------------------------------------------")
				print("goods list : ",end="")
				print(goods["list"])
				print("goods prices : ",end="")
				print(goods["prices"])
				h=int(input("Which element u want to Buy : "))		#what to buy
				k=int(input("Enter The Amount u want to Buy : "))	#amount
				j=h-1
				list1=goods["list"]
				list2=goods["stocks"]
				list3=goods["prices"]
				buying_list.append(list1[j])
				total=(list3[j]*k)+total
				buying_amount.append(k)
				buying_price.append(k)
				list2[j]=list2[j]-k
				goods.setdefault("stocks", list2)
				listprice.append(list3[j])
				print(buying_list)
				print(buying_amount)
				print(total)
				print("-----------------------------------------------")
			elif customer==2:
				print("-----------------------------------------------")
				print(buying_list)
				print("-----------------------------------------------")
			elif customer==3:
				print("-----------------------------------------------")
				table=PrettyTable()
				print("The list of items have been bought : ",buying_list)
				print("Price of each item",listprice)
				print("The amounts of items in KGs : ",buying_amount)
				table.add_column('List of Items',buying_list)
				table.add_column('Price',listprice)
				table.add_column('Amount',buying_amount)
				print(table)
				print("The Total Bill : ",total)

				listtotal.append(total)
				
				d = {"Items": buying_list, 
				"Item Price":listprice, 
				"Amount in KGs": buying_amount,
				}
				
			
				with open("customer.csv", "w") as outfile:
    
			
					writerfile = csv.writer(outfile)
      
			
					writerfile.writerow(d.keys())
      
			
					writerfile.writerows(zip(*d.values()))
				t = time.localtime()
				current_time = time.strftime("%H:%M:%S", t)
				print(current_time)
				print("-----------------------------------------------")
			elif customer==0:
				customer=0
				break;
			else:
				print("Wrong Entry,Try again.")
	elif (mode=='0'):
		x=0
	else:
		print("Wrong Entry try again.")