def check_numbeer(age):
    if age >= 20:
        return"会員"
    else:
        return"非会員"
print(check_numbeer(25))
print(check_numbeer(15))