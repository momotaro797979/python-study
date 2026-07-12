def muryou(age,has_disability):
    if age >= 65 or has_disability:
        return"無料"
    else:
        return"有料"
print(muryou(40,True))