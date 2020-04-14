def alternatingSums(a):
    together = []
    teamA = sum(a[::2])
    teamB = sum(a[1::2])
    together.append(teamA)
    together.append(teamB)
    return together  
