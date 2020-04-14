def circleOfNumbers(n, firstNumber):
    output = list(range(0,n))
    half = len(output)//2
    
    if firstNumber < half:
        return half + firstNumber
    else:
        return abs(half - firstNumber)
