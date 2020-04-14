def alphabeticShift(Input):
    import string

    alphabet = list(string.ascii_lowercase)
    Input = list(Input)
    
    for i in range(len(Input)):
        index = 0
        if Input[i] != "z":
            index = alphabet.index(Input[i]) + 1
        Input[i] = alphabet[index]

    return "".join(Input)
