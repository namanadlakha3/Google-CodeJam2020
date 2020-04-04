def solve():
    s = input() + "0"
    sn = ""
    curr = 0
    for ch in s:
        n = ord(ch)-48
        if curr < n:
            sn += (n-curr) * '('
            curr = n
        elif n < curr:
            sn += (curr-n) * ')'
            curr = n
        sn += ch
    return sn[:-1]

t = int(input())
for i in range(1, t+1):
    s = solve()
    print("Case #{}: {}".format(i, s))