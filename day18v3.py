def grade(score):
    if score >= 90:
        return("S")
    elif score >= 80:
        return("A")
    else:
        return("B")
print(grade(95))