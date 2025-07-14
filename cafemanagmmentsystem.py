menu ={
    'burger' : 20,
    'coffee' : 15,
    'pizza'  : 30
}

print("Welcome to my restaurant")
print("pizza  : 30\nBurger : 20\ncoffee : 15")
order_total = 0
item_1 = input("Enter the name of item you want")
if item_1 in menu :
    order_total += menu[item_1]
else:
    print(f"ordered item {item_1} is not available")

another_order = input("Do you want another item (yes\\no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item")
    order_total += menu[item_2]
    print(f"Item{item_2} has been added to order")
else:
     print("This is not available")

print(f"The total amount of items to pay is {order_total}")




