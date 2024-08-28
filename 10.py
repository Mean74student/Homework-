# EX10.Show product name that has maximum price
def max_price(price):
    max = 0
    products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
    for price in products:
        if price["price"] > max:
            max = price["price"]
    return max
print(max_price(max))