def reverseInParentheses(Input):
    output = []
    
    for i in Input:
        if i == ")":
            Save = []
            Bin = output.pop()
            while Bin != "(" :
                Save.append(Bin)
                Bin = output.pop()
            output += Save
        else:
            output.append(i)

    return "".join(output)
