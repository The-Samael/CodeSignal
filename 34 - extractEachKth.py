def extractEachKth(Input, k):
    del Input[k-1::k]
    return Input
