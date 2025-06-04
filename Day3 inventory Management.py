inventory = {"apple": 50,
             "banana": 100,
             "cucumber": 25,
             "soap": 100,
             "tooth paste": 30,
             "tooth brush": 45,
             "hand wash": 18,
             "milk": 20,
             "biscuits": 120,
             "chocolates": 8}
cart = {}
print('''
-----------------------------
Welcome to AJR SUPER MARKET
-----------------------------
1. View Inventory
2. Buy Item
3. Add/ModifyInventory (Authorised User Only)
4. Exit''')
while True:
    user_input = input("Enter your Choice:")
    try:
        if int(user_input) == 1:
            print("Current Inventory")
            for item in inventory:
                print(item, "-", inventory[item], "Numbers")
        elif int(user_input) == 2:
            while True:
                x = input("Enter the item you want to purchase: ")
                qty = int(input("Enter the quantity: "))
                if x in cart:
                    cart[x] += qty
                    inventory[x] -= qty
                else:
                    cart[x] = qty
                    inventory[x] -= qty
                y = input("Want to purchase more? yes or no:").lower()
                if y != "yes":
                    break
            print("You have added")
            for item in cart:
                print(item, "-", cart[item], "Numbers")

        elif int(user_input) == 3:
            print("You are supposed to add or modify the inventory, So Please confirm")
            a = input("Are you a staff? Yes or No: ")
            if a == "Yes" or a == "YES" or a == "yes":
                b = int(input("Enter your staff code:"))
                if b in range(1800, 1901):
                    # Adding quantity
                    inventory["apple"] += 5
                    # Adding new items
                    inventory["orange"] = 30
                    # deleting inventory
                    del inventory["chocolates"]
                    for item in inventory:
                        print(item, "-", inventory[item], "Numbers")
                else:
                    print("Not a valid staff code")
            else:
                print("Not authorised to add Inventory")
        elif int(user_input) == 4:
            print("Thanks for shopping")
            break
        else:
            print("Enter Valid Input")
    except ValueError:
        print("Error: Please enter a valid number.")