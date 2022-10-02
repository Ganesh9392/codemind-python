def printCountDP(dist):
    count = [0] * (dist + 1)
    count[0] = 1
    if dist >= 1 :
        count[1] = 1
    if dist >= 2 :
        count[2] = 2
    for i in range(3, dist + 1):
        count[i] = (count[i-1] +
                   count[i-2] + count[i-3])
    return count[dist]
dist = int(input())
print( printCountDP(dist))