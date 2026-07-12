def add_tax(price):
    return price * 1.1
price = add_tax(800)
if price >= 1000:
    print("高い")
else:
    print("安い")
