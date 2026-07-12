def withdraw(balance,has_card):
    if balance >=1000 and has_card:
        return"引き出せます"
    else:
        return"引き出せません"
print(withdraw(500,True))
