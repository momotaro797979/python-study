def can_take_exam(age,cashed):
    if age >= 18 and cashed:
        return"受験できます"
    else:
        return"受験できません"
print(can_take_exam(22,True))