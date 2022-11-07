goods={
"list": ["apple","banana","cherry","mango"],
"prices":[10	,	8	,	25	,	18],
"stocks":[25	,	40	,	10	,	20],
}
customer=1
owner=1
list1=[]
list2=[]
list3=[]
listprice=[]
buying_list=[]
buying_price=[]
buying_amount=[]
total=0
while(1):
	print("------------ Welcome to ITI Grocery Shop ------------")
	mode=input("(1)Customers \n(2)the Owner \n(0)Exit\n")
	print("-----------------------------------------------")
	if mode=='2':
		while(owner):
			owner=int(input("(1)Show Products \n(2)Add Products \n(3)Change Cost \n(0)Exit\n"))
			if owner==1:
				print("-----------------------------------------------")
				print(goods.items())
				print("-----------------------------------------------")
				
			elif owner==2:
				print("-----------------------------------------------")
				product=input("Enter Product Name : ")
				product=product.lower()
				goods["list"].append(product)
				price=int(input("Enter the product price : "))
				goods["prices"].append(price)
				stock=int(input("Enter the Amount : "))
				goods["stocks"].append(stock)
				print("-----------------------------------------------")
			elif owner==3:
				print("-----------------------------------------------")
				e=int(input("Which element u want to change its price : "))
				price=int(input("Enter the new product's price : "))
				p=e-1
				goods["prices"].pop(p)
				goods["prices"].insert(p,price)
				print("-----------------------------------------------")
			elif owner==0:
				print("-----------------------------------------------")
				break;
			else:
				print("-----------------------------------------------")
				print("Wrong Entry , Try again.")
				print("-----------------------------------------------")
	elif mode=='1':
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
				print("The list of items have been bought : ",buying_list)
				print("Price of each item",listprice)
				print("The amounts of items in KGs : ",buying_amount)
				print("The Total Bill : ",total)			
			elif customer==0:
				break;
			else:
				print("Wrong Entry,Try again.")
	elif (mode=='0'):
		break;
	else:
		print("Wrong Entry try again.")