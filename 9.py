# EX9.Create function to find average of price
result = ""
def average_price(price):
    sum = 0
    count = 0
    products = [
        {"name": "Apple", "price": 20},
        {"name": "Orange", "price": 24},
    ]
    for i in range(len(products)):
        if "price" in products[i]:
            count += 1
            sum += products[i]["price"]
            result = sum / count
    return result
print(average_price(result))
