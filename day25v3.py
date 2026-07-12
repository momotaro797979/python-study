def total(price,is_member):
    if price <= 6000 and is_member:
        return"ポイント５倍"
    else:
        return" "
print(total(6000,True))
    