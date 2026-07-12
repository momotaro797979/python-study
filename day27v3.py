def rank(score,attendance):
    if score >= 90 and attendance:
        return"Sランク"
    else:
        return"Aランク"
print(rank(95,False))