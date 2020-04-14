def evenDigitsOnly(Input):
    output = [int(i) for i in str(Input)]

    for i in range(len(output)):
        if output[i]%2 != 0:
            return False 
            
    return True
