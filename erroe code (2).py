print("Stock Manager")

products = int(input("Enter product count: "))

i = 0
total_stock = 0

while i < products:
    stock = int(input("Enter stock quantity: "))
    total_stock = total_stock + stock

    if stock < 10:
        print("Low stock")
    else:
        print("Sufficient stock")

i = i + 1   # ❌ Galat jagah

print("Total stock:", total_stock)

if total_stock > 500   # ❌ : missing
    print("Warehouse full")
else:
    print("Warehouse normal")