def isLucky(n):
    n = str(n)
    n = list(n)

    half = len(n)//2
    first_list = n[0:half]
    second_list = n[half:]

    first_half = []
    second_half = []

    for i in first_list:
        first_half.append(int(i))
    for j in second_list:
        second_half.append(int(j))

    
    return sum(first_half) == sum(second_half)
