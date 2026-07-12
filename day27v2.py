def shipping(total,is_member):
    if total <= 50000 or is_member:
        return"送料無料"
    else:
        return"送料有料"
print(shipping(3000,True))