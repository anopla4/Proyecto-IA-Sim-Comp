def tokenize(s, t):
    tokens = [""]
    for i in s:
        if i in t:
            tokens.append(i)
            tokens.append("")
        else:
            tokens[-1] += i
    return list(filter(lambda x: x != "", tokens))
