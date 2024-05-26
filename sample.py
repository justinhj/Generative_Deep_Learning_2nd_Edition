def encode(ids):
    out = []
    i = 0
    while True:
        # 0 1 2 3
        # a b c d
        if i < len(ids) - 1 and (ids[i], ids[i + 1]) in merges:
            out.append(merges[(ids[i], ids[i + 1])])
        else:
            out.append(ids[i])
    return out
