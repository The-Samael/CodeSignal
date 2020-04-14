def boxBlur(image):
    output = []
    for i in range(1, len(image) - 1):
        Bin = []
        for j in range(1, len(image[i]) - 1):
            square = (image[i-1][j-1]
                      +image[i-1][j]
                      +image[i-1][j+1]
                      +image[i][j-1]
                      +image[i][j]
                      +image[i][j+1]
                      +image[i+1][j-1]
                      +image[i+1][j]
                      +image[i+1][j+1])
            Bin.append(square//9)
        output.append(Bin)
    return output
