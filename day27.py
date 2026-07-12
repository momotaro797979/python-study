def can_enter(age,is_member):
    if age >= 18 and is_member:
        return"入場できます"
    else:
        return"入場できません"
print(can_enter(20,True))