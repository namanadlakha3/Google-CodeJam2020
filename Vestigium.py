def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append([int(j) for j in input().split()])
    #print(arr)
    diag = 0
    col = 0
    row = 0
    for i in range(n):
        c = []
        r = []
        cf = 0
        rf = 0
        for j in range(n):
            if arr[i][j] in r:
                rf = 1
            else:
                r.append(arr[i][j])
            if arr[j][i] in c:
                cf = 1
            else:
                c.append(arr[j][i])
            if i==j:
                diag += arr[i][j]
        col += cf
        row += rf
        c.clear()
        r.clear()            
    return "{} {} {}".format(diag, row, col)

t = int(input())
for i in range(1, t+1):
    s = solve()
    print("Case #{}: {}".format(i, s))