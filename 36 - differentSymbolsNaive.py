def differentSymbolsNaive(s):
    output = list(s)
    diff = []
    for i in output:
        if i not in diff:
            diff.append(i)
    return len(diff)
