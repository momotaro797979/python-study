def check_age(age):
    if age % 18 < 0:
        return "大人"
    else:
        return"子ども"
print(check_age(15))