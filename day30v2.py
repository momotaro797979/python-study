def movie_fee(age,student):
    if age < 18:
        return"子ども料金"
    elif age <= 18 and student:
        return"学生料金"
    else:
        return"一般料金"
print(movie_fee(45,True))