fruits = ["Apple", "Banana", "Mango", "Orange"]
prices = [250, 140, 290, 180]

VAT_PCT = 0.13
price_after_vat = []

def add_vat(num):
    VAT_PCT = 0.13
    return num + (num * VAT_PCT)

for price in prices:
    price_after_vat.append(add_vat(price))

print(price_after_vat)
print(prices)

# for price in prices:
#     final_price = price + (price * VAT_PCT)
#     price_after_vat.append(final_price)

# print(price_after_vat)
# print(prices)


# for i in range(4):
#     print(f"The price of {fruits[i]} is {prices[i]}.")

# new_prices = []

# for price in prices:
#     new_prices.append(price + 100)

# print(new_prices)
# print(prices)