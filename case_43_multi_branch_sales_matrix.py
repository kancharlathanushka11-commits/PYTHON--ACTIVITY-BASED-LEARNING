# Case 43: Multi-Branch Sales Matrix Comparison

branches = ["Branch 1", "Branch 2", "Branch 3"]
products = ["Laptop", "Mobile", "Tablet"]

# Sales data: each branch contains daily sales for each product
sales = [
    [[10, 12, 8], [15, 10, 5], [6, 8, 4]],
    [[12, 10, 9], [10, 14, 6], [8, 7, 5]],
    [[15, 12, 10], [8, 9, 7], [5, 6, 4]]
]

branch_totals = []

for i in range(len(branches)):
    print("\n", branches[i])
    total_branch = 0

    for j in range(len(products)):
        total_product = sum(sales[i][j])
        total_branch += total_product
        print(products[j], "Total Sales:", total_product)

    branch_totals.append(total_branch)
    print("Total Branch Sales:", total_branch)

    best_product_index = 0

    for j in range(1, len(products)):
        if sum(sales[i][j]) > sum(sales[i][best_product_index]):
            best_product_index = j

    print("Best Performing Product:", products[best_product_index])

# Compare branches
best_branch_index = branch_totals.index(max(branch_totals))
print("\nBest Performing Branch:", branches[best_branch_index])
print("Highest Branch Sales:", branch_totals[best_branch_index])
