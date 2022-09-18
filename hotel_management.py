import datetime

print("\nWelcome To Hotel Euphoria\n")

print("      ******** TAMIL FOODS ONLY ********")

print("1- BREAKFAST        2- LUNCH         3- DINNER\n")


def break_fast():
    bf_menu = ["Dosa", "Idly", "Poori", "Vada"]

    dosa = 50
    idly = 30
    poori = 50
    vada = 7

    options = input("Do You Want to Menu: Y/N: ")
    if options == "Y":
        print("\n----------------------")
        print(*bf_menu, sep="\n")
        print("----------------------\n")
    else:
        return break_fast()
    order_list = input("Enter the Food You Want: ")
    if order_list in bf_menu:
        print(f"yes! {order_list} is Available")

        if order_list == "Dosa":
            print("Price : Rs/- 50")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*dosa
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if order_list == "Idly":
            print("Price : Rs/- 30")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*idly
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if order_list == "Poori":
            print("Price : Rs/- 50")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*poori
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if order_list == "Vada":
            print("Price : Rs/- 7")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*vada
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")

    
    
def lunch():
    lunch_menu = ["Chicken Biriyani", "Meals", "Tomato Rice", "Lemon Rice"]
    chicken = 120
    meals = 100
    tomato = 60
    lemonrice = 60

    lunch_options = input("Do You Want to Menu: Y/N: ")
    if lunch_options == "Y":
        print("\n----------------------")
        print(*lunch_menu, sep="\n")
        print("----------------------\n")
    else:
        return break_fast()
    lunch_order_list = input("Enter the Food You Want: ")
    if lunch_order_list in lunch_menu:
        print(f"yes! {lunch_order_list} is Available")

        if lunch_order_list == "Chicken Biriyani":
            print("Price : Rs/- 120")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*chicken
            pdate= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if lunch_order_list == "Meals":
            print("Price : Rs/- 100")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*meals
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if lunch_order_list == "Tomato Rice":
            print("Price : Rs/- 60")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*tomato
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if lunch_order_list == "Lemon Rice":
            print("Price : Rs/- 60")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*lemonrice
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")


def dinner():
    dinner_menu = ["Chicken Biriyani", "Dosa", "Chappathi", "Omlette"]
    c_biriyani = 120
    dosa = 50
    chappathi = 40
    omlette = 20

    dinner_options = input("Do You Want to Menu: Y/N: ")
    if dinner_options == "Y":
        print("\n----------------------")
        print(*dinner_menu, sep="\n")
        print("----------------------\n")
    else:
        return dinner()

    dinner_order_list = input("Enter the Food You Want: ")
    if dinner_order_list in dinner_menu:
        print(f"yes! {dinner_order_list} is Available")
        if dinner_order_list == "Chicken Biriyani":
            print("Price : Rs/- 120")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*c_biriyani
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if dinner_order_list == "Dosa":
            print("Price : Rs/- 50")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*dosa
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if dinner_order_list == "Chappathi":
            print("Price : Rs/- 40")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*chappathi
            date= datetime.datetime.now()
            f=open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")
            
        if dinner_order_list == "Omlette":
            print("Price : Rs/- 20")
            dn_qty = int(input("\nHow Much: \n"))
            total_d_bill = dn_qty*omlette
            date = datetime.datetime.now()
            f = open("bill.txt", "w")
            f.write(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print(f"Total Amount is Rs/-{total_d_bill} \n {date}\n")
            print("\nBill Downloaded\n")

choose_what = int(input("Choose: "))

if choose_what == 1:
    break_fast()
elif choose_what == 2:
    lunch()
elif choose_what == 3:
    dinner()
