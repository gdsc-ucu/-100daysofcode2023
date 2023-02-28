"""Using dynamic functions, demonstrate with an interactive program that reads from the keyboard the name of the customer, the name of the commodity he is buying, the price of the commodity, the dates, and the cashier's name.


1. You should be able to get the price of the commodity and subtract VAT of 18%
2. Print out the actual NET sale of the product, the name of the customer and name of the cashier and the date
3. Print the name of the software developers and the copyright
"""


import datetime

# Define function to calculate net sale price after VAT
def calculate_net_sale(price):
    net_sale = price * (1 - 0.18)
    return net_sale

# Define function to read input from user
def get_input(prompt):
    user_input = input(prompt)
    return user_input

# Define function to print receipt
def print_receipt(customer_name, commodity_name, price, cashier_name):
    net_sale = calculate_net_sale(price)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("--------------- RECEIPT ---------------")
    print(f"Customer name: {customer_name}")
    print(f"Commodity name: {commodity_name}")
    print(f"Gross sale price: {price}")
    print(f"Net sale price: {net_sale}")
    print(f"Cashier name: {cashier_name}")
    print(f"Date: {date}")
    print("--------------------------------------")

# Define function to print software information
def print_software_info():
    print()
    print("Developed by Ashaba Jasper and Deborah Patience")
    print("Copyright © 2023")

# Get input from user
customer_name = get_input("Enter customer name: ")
commodity_name = get_input("Enter commodity name: ")
price = float(get_input("Enter commodity price: "))
cashier_name = get_input("Enter cashier name: ")
print()

# Print receipt and software information
print_receipt(customer_name, commodity_name, price, cashier_name)
print_software_info()
