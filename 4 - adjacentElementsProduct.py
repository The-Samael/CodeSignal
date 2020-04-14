def adjacentElementsProduct(inputArray):
    Bin = []
    for x in range(len(inputArray) - 1):
        Bin.append(inputArray[x] * inputArray[x + 1])
    return max(Bin)
