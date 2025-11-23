from tabulate import tabulate
from datetime import datetime

# Stored in memory (nothing is stored in files)
inventory={}

# Add the medicines
def add_medicine():
    name=input("Enter medicine name: ").title()
    quantity=int(input("Enter quantity: "))
    expiry=input("Enter expiry date (DD-MM-YYYY): ")
    inventory[name] = {"quantity": quantity,"expiry": expiry}
    
    print("\n"+name+" added successfully!\n")

# View your inventory
def view_inventory():
    if not inventory:
        print("\nInventory is empty.\n")
        return

    table_data=[]
    for name,details in inventory.items():
        table_data.append([name,details["quantity"],details["expiry"]])

    print("\nMedicine Inventory:")
    print(tabulate(table_data, headers=["Name","Quantity","Expiry Date"],tablefmt="grid"))
    print()

# Checking stock of medicines
def show_low_stock():
    print("\nLow Stock Medicines (<= 5):")
    low_stock_items=[[name, details["quantity"]]
        for name, details in inventory.items()
        if details["quantity"]<= 5
    ]

    if low_stock_items:
        print(tabulate(low_stock_items, headers=["Name", "Quantity"], tablefmt="grid"))
    else:
        print("No low stock medicines.")
    print()

# Expired medicines
def show_expired():
    print("\nExpired Medicines:")

    expired_list=[]
    today=datetime.now()                           # It gives us the current date

    for name,details in inventory.items():
        exp_date=datetime.strptime(details["expiry"], "%d/%m/%Y")
        if exp_date<today:
            expired_list.append([name, details["expiry"]])

    if expired_list:
        print(tabulate(expired_list, headers=["Name", "Expiry Date"], tablefmt="grid"))
    else:
        print("No expired medicines.\n")
    print()
    
# Removing meicines
def remove_medicine():
    if not inventory:
        print("\nInventory is empty!Nothing to remove.\n")
        return

    name = input("Enter the medicine name to remove: ").title()

    if name in inventory:
        confirm = input(f"Are you sure you want to remove{name}?(y/n):").lower()
        if confirm == "y":
            del inventory[name]
            print("\n"+{name}+"removed successfully!\n")
        else:
            print("\nCancelled. Medicine was not removed.\n")
    else:
        print("\nMedicine not found in inventory.\n")

# Selecting choices
def menu():
    while True:
        print("=== Medicine Inventory System ===")
        print("1.Add Medicine")
        print("2.View Inventory")
        print("3.Show Low Stock")
        print("4.Show Expired Medicines")
        print("5.Remove Medicine")
        print("6.Exit")

        choice = input("Enter your choice: ")

        if choice=="1":
            add_medicine()
        elif choice=="2":
            view_inventory()
        elif choice=="3":
            show_low_stock()
        elif choice=="4":
            show_expired()
        elif choice=="5":
            remove_medicine()
        elif choice=="6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")
menu()