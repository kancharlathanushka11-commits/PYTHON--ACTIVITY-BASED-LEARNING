# Case 46: Inventory Matrix Reconciliation

warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]
products = ["Pens", "Books", "Bags"]

stock = [
    [100, 40, 15],
    [80, 60, 20],
    [70, 50, 10]
]

targets = [300, 180, 50]

for j in range(len(products)):
    total = 0

    for i in range(len(warehouses)):
        total += stock[i][j]

    difference = total - targets[j]

    print(products[j], "total stock:", total, "target:", targets[j])

    if difference < 0:
        print("Shortage:", -difference)
    elif difference > 0:
        print("Surplus:", difference)
    else:
        print("Stock exactly meets target")
