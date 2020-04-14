def allLongestStrings(inputArray):
    length = len(inputArray[0])
    Bin = []
    for i in range(1,len(inputArray)):
        if length < len(inputArray[i]):
            length = len(inputArray[i])
    for word in inputArray:
        if len(word) == length:
            Bin.append(word)
    return Bin
