def can_can_watch_movie(age,money):
    if age >= 20 and money >= 3000:
        return"映画に行けます"
    else:
        return"映画に行けません"
print(can_can_watch_movie(25,5000))
