

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt

#input
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

#process
subtotal = item_price * quantity
discount = subtotal * (discount_percent / 100)
price = subtotal - discount
tax = price + (tax_percent / 100)
final_total = price + tax

#output
print("subtotal =", subtotal)
print(f"discount {discount}")
print(f"tax percent: {tax_percent}")
print(f"final price {final_total}")