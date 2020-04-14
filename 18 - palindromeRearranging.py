def palindromeRearranging(Input):
    Bin = []
    Count = []
    oddCount = 0

    for i in Input:
        while i not in Bin:
            Bin.append(i)
    
    for i in range(len(Bin)):
        Count.append(Input.count(Bin[i]))

    for i in range(len(Count)):
        if Count[i]%2 != 0:
            oddCount += 1
    
    if oddCount > 1:
        return False
    else:
        return True
