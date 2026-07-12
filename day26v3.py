def deliverry(price,is_premium):
    if price >= 10000 or is_premium:
        return"VIP配送"
    else:
        return"通常配送"
print(deliverry(80000,True))