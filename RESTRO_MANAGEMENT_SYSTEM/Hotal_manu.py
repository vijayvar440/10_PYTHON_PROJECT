manu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salade':70,
    'coffee':80
}
print("welcome may python resturent")
print("pizza : RS 40 \n pastta : RS 50 \n burger : 60 \n salade : 70 \n coffee : 80")

order_total = 0 
item_1 = input("enter the name of the item you want to order = ")

if item_1 in manu:
    order_total += manu[item_1]
    print(f"your iteam {item_1} has been added to your order ")
else:
    print(f"oredr item {item_1} is not avaialable yet")  

another_order = input("do you wont another order (yes/no)? ")    
if another_order == "yes":
    item_2 = input("enter the name of second iteam + ")
    if item_2 in manu:
        order_total += manu[item_2]
        print(f"iteam {item_2} has been added to order ")
    else:
        (f"order item {item_2} is not avaialable")

print(f"The total amount of items to is {order_total}")