def shipping(price,is_member):
    if price >= 10000 or is_member:
        return"送料無料"
    else:
        return"送料500円"    
print(shipping(50,True))