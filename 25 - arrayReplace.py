def arrayReplace(Input, WhatR, Replace):
    for i in range(len(Input)):
        if Input[i] == WhatR:
            Input[i] = Replace
    return Input
