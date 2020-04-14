def areSimilar(a, b):
    A = []
    B = []
    for i in range(len(a)):
        if a[i] != b[i]:
            A.append(a[i])
            B.append(b[i])

    B.reverse()
    
    if str(a) == str(b):
        return True
    
    if len(B) == 2 and str(A) == str(B):
        return True
    else:
        return False
