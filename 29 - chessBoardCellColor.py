def chessBoardCellColor(cell1, cell2):

    alphabet = ["A","B","C","D","E","F","G","H"]
    numbers = ["1","2","3","4","5","6","7","8"]

    cell1 = list(cell1)
    cell2 = list(cell2)

    match1 = 0
    match2 = 0

    indexL1 = alphabet.index(cell1[0])
    indexL2 = alphabet.index(cell2[0])
    indexN1 = numbers.index(cell1[1])
    indexN2 = numbers.index(cell2[1])
 
    if (indexL1+indexN1)%2 == 0:
        match1 += 1
    if (indexL2+indexN2)%2 == 0:
        match2 += 1

    return match1 == match2
