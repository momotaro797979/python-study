def shippping_fee(price,has_member):
    if price <= 5000 or has_member:
        return"送料無料"
    else:
        return"送料500円"
print(shippping_fee(3000,True))