def knapsackLight(value1, weight1, value2, weight2, maxW):
    Bin = []
    Bin.append(value1)
    Bin.append(value2)

    if weight1 + weight2 <= maxW:
        return value1 + value2
    if weight1 + weight2 >= maxW and weight1 <= maxW and weight2 <= maxW:
        return max(Bin)
    if maxW < weight1 and maxW < weight2:
        return 0
    if maxW >= weight1 and maxW < weight2:
        return value1
    if maxW < weight1 and maxW >= weight2:
        return value2
