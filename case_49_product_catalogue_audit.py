# Case 49: Tuple-Based Product Catalogue Audit

products = [
    ("P101", 25.0, 30),
    ("P102", 120.0, 6),
    ("P103", -5.0, 12),
    ("P104", 50.0, 0)
]

reorder_level = 10

for product in products:
    product_id, price, quantity = product

    if product_id == "" or price < 0 or quantity < 0:
        print(product_id, "INVALID RECORD")
        continue

    value = price * quantity
    print(product_id, "inventory value:", round(value, 2))

    if quantity < reorder_level:
        print(product_id, "requires replenishment")
