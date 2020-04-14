def isIPv4Address(Input):
    output = []

    for i in Input:
        output =  Input.split('.')  

    for i in output:
       if len(i) > 1 and i[0] == "0":
           return False

    for i in output:
        if not i.isdecimal():
            return False 

    for i in range(0,len(output)):
        output[i] = int(output[i])
    
    if len(output) != 4:
        return False
    if Input.count(".") != 3:
        return False
    if max(output) > 255:
        return False

    return True
