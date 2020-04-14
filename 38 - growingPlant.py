def growingPlant(upSpeed, downSpeed, desiredHeight):
    output = 0
    count = 0
    while output < desiredHeight:
        output += upSpeed
        count += 1
        if output < desiredHeight:
            output -= downSpeed
    return count
