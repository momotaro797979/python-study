def check_rank(rank):
    if rank >= 100:
        return"ゴールド"
    elif rank >= 50:
        return"シルバー"
    else:
        return"ブロンズ"
print(check_rank(120))