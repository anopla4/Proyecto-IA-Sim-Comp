from .token import Token


def tokenize(s, word_type, t):
    tokens = []
    _tokens = [""]
    for (index, i) in enumerate(s):
        if (
            len(_tokens) > 0
            and len(_tokens[-1]) > 0
            and _tokens[-1][-1] == "\\"
            and i in t
        ):
            _tokens[-1] += i
            if index == len(s) - 1:
                tokens.append(Token(_tokens[-1], word_type))
        elif i in t:
            if len(_tokens) > 0 and _tokens[-1] == "":
                _tokens.pop(-1)
            if len(_tokens) > 0 and _tokens[-1] not in t:
                tokens.append(Token(_tokens[-1], word_type))
            _tokens.append(i)
            tokens.append(Token(i, t[i]))
            _tokens.append("")
        else:
            _tokens[-1] += i
            if index == len(s) - 1:
                tokens.append(Token(_tokens[-1], word_type))
    return tokens
