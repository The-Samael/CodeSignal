def addBorder(picture):
    lenght = len(picture[0])
    wall = ""
    output = []

    for i in picture:
        output.append("*" + i+ "*")
    for j in range(lenght+2):
        wall = wall + "*"
    
    output.append(wall)
    output.insert(0,wall)

    return output
