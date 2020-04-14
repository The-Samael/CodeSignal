def firstDigit(Input):
    output = list(Input)
    num = []
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for i in output:
        if i in numbers:
            num.append(i)
    return num[0]
