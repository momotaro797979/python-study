def can_buy(money,has_qupon):
    if money <= 7000 or has_qupon:
        return"購入できます"
    else:
        return"購入できません"
print(can_buy(5000,True))
