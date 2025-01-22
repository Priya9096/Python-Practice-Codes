d = {}
while True:
    user_input = input().strip()
    if user_input == 'done':
        break
    product_name,price = user_input.split(',')
    product_name = product_name.strip()
    price = float(price.strip())
    d[product_name] = price

for name, price in d.items():
    print(f"{name}: {price}")
    

