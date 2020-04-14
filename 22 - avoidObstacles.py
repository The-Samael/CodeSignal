def avoidObstacles(Input):
    Input = sorted(Input)
    last = max(Input)
    
    for i in range(2, last + 2):
        done = True
        output = i
        while output < (last + i):
            if output in Input:
                done = False
                break
            output += i
        if done:
            return i
