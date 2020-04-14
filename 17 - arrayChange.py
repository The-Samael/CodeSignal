def arrayChange(Input):
    count = 0

    for i in range(len(Input)-1):
        if Input[i] >= Input[i + 1]:
            diff = Input[i] + 1 - Input[i + 1]
            Input[i + 1] = Input[i] + 1 
            count += diff

    return count
