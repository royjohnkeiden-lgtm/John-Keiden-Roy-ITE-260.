#Border--
print("=====================================")
print("         Aling Masing SHOP")
print("=====================================")

#Customer and Employees info
cashier = input("\nCashier: ")
customer = input("Customer: ")

#Product1 
item1 = input("\nItem1: ")
quantity = float(input("Quantity: "))
price = float(input("Price: "))

subtotal1 = quantity * price

#Product2
item2 = input("\nItem2: ")
quantity = float(input("Quantity: "))
price = float(input("Price: "))

subtotal2 = quantity * price

#Product3
item3 = input("\nItem3: ")
quantity = float(input("Quantity: "))
price = float(input("Price: "))

subtotal3 = quantity * price
total = subtotal1 + subtotal2 + subtotal3

print("\n--------------------------------------")
print("               RECEIPT")
print("--------------------------------------")

print("\nItem:", item1)
print("Quantity:", quantity)
print("Price:", price)

print("\nItem:", item2)
print("Quantity:", quantity)
print("Price:", price)

print("\nItem:", item3)
print("Quantity:", quantity)
print("Price:", price)

print("\nTotal:", total)
print("--------------------------------------")

payment = float(input("\nCash received: "))

change = payment - total
print("Change:", change)

if payment <= total:
    print("Balik ka na lang!")

print("=====================================")
print("         Arigatōgozaimasu")
print("=====================================")
