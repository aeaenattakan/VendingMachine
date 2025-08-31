print("---Welcome to Mark's Coffee---")
while True:
    menu = input("Please type 1 to show menu: ")
    if menu == "1":
        print("""---Choose the menu---
	1. Espresso
	2. Cappuccino
	3. Latte""")
        while True:
            coffee = input("Select coffee: ")
            if coffee.isdigit() and int(coffee) in [1, 2, 3]:
                coffee = int(coffee)
                coffee_names = {
                    1: "Espresso",
                    2: "Cappuccino",
                    3: "Latte"
                }
                print("""---Choose the type of the coffee---
    1. Hot 55 baht
    2. Cold 60 baht""")
                while True:
                    coffee_type = input("Select type: ")
                    if coffee_type.isdigit() and int(coffee_type) in [1, 2]:
                        coffee_type = int(coffee_type)
                        if coffee_type == 1:
                            print("---You chose hot %s 55 baht---" % (coffee_names[coffee]))
                            total_money = 0
                            while total_money < 55:
                                money = float(input("Input your money:"))
                                if money < 0:
                                    print("""Money cannot be negative
---Please try again---""")
                                else:
                                    total_money += money
                                    if total_money >= 55:
                                        print("""You received a change of %.2f baht
---Thank you---""" % (total_money - 55))
                                        break
                                    else:
                                        print("""Not enough money
You need to add %.2f more baht""" % (55 - total_money))
                        elif coffee_type == 2:
                            print("---You chose cold %s 60 baht---" % (coffee_names[coffee]))
                            total_money = 0
                            while total_money < 60:
                                money = float(input("Input your money:"))
                                if money < 0:
                                    print("""Money cannot be negative
---Please try again---""")
                                else:
                                    total_money += money
                                    if total_money >= 60:
                                        print("""You received a change of %.2f baht
---Thank you---""" % (total_money - 60))
                                        break
                                    else:
                                        print("""Not enough money
You need to add %.2f more baht""" % (60 - total_money))
                        break
                    else:
                        print("""Sorry, something went wrong
Please choose 1(Hot) or 2(Cold) only""")
                break
            else:
                print("""Sorry, something went wrong
Please choose 1(Espresso) or 2(Cappuccino) or 3(Latte) only""")
                break
    else:
        print("""Sorry, something went wrong
Please type 1 only""")