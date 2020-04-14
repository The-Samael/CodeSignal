def arrayMaximalAdjacentDifference(Input):
    number = []
    Bin = ()
    for i in range(len(Input)-1):
        Bin = abs(Input[i]-Input[i+1])
        number.append(Bin)
    return max(number)
