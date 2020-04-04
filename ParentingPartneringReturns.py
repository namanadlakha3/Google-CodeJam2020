import sys

def Solve(N, schedules):
    answer = ""

    t1 = 0
    t2 = 0

    schedules.sort()
    answers = ['' for x in range(N)]

    for s, e, n in schedules:
        if s >= t1:
            t1 = e
            answers[n] = 'C'
        elif s >= t2:
            t2 = e
            answers[n] = 'J'
        else:
            return "IMPOSSIBLE"

    for x in answers:
        answer += x
        
    return answer

rl = lambda: sys.stdin.readline()

T = int(rl())
for t in range(T):
    N = int(rl())
    schedules = []
    for n in range(N):
        s, e = [int(x) for x in rl().split()]
        schedules.append((s, e, n))
    print("Case #%d: %s" % (t + 1, Solve(N, schedules)))