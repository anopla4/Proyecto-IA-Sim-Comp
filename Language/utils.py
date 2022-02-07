def all_productions(productions):
    all_productions = [i for i in productions.values()]
    _productions = []
    for p in all_productions:
        _productions += p
    return _productions
