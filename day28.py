def membership(age,is_member):
    if age >= 20 and is_member:
        return"VIP会員"
    else:
        return"一般会員"
print(membership(25,True))