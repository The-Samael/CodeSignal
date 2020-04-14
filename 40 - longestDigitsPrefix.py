def longestDigitsPrefix(Input):
    Input = list(Input)
    num = ["0","1","2","3","4","5","6","7","8","9"]
    output = []

    for i in range(len(Input)):
        if Input[i] in num:
            output.append(Input[i])
        else:
            break

    return "".join(output)
