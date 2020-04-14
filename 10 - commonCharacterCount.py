def commonCharacterCount(s1, s2):
    count = 0
    Bin = list(s2)
    for i in s1:
        if i in Bin:
            Bin.remove(i)
            count += 1
    return count
