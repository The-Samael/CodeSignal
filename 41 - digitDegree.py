def digitDegree(n):
    output = [int(i) for i in str(n)]
    count = 0

    if len(output) == 1:
        return 0
    if len(str(sum(output))) == 1:
        return 1
    else:
        while True:
            count += 1
            output = [int(i) for i in str(sum(output))]
            if len(output) == 1:
                break
    return count
