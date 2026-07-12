def movie_price(age):
    if age >= 60:
        return"シニア料金"
    elif age >= 18 and age < 60:
        return"一般料金"
    else:
        return"子ども料金"
print(movie_price(12))