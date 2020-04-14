def sortByHeight(a):
    duplicate = []
    count = 0
    
    for x in a:
        if not x == -1:
            duplicate.append(x)

    duplicate.sort()

    for i in range(len(a)):
        if a[i] != -1:
            a[i] = duplicate[count]
            count += 1

    return a
