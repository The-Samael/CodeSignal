def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft == friendsLeft and yourRight == friendsRight:
        return True
    if  yourLeft == friendsRight and yourRight == friendsLeft:
        return True
    else:
        return False
