# EX8.Create function to sum total of price 
def sum_price(price):
    sum = 0
    products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
    for price in products:
        sum += price["price"]
    return sum
print(sum_price(sum))