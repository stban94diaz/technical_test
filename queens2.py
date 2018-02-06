n = 8

def queens(nR=0, solution=[-1 for i in range(n)], cols=[], d45=[], d135=[]):
    if nR == n:
        m = [['0' for i in range(n)] for j in range(n)]
        for i in range(len(solution)):
            m[i][solution[i]] = 'x'
        for row in m:
            print(row)
        input("Press key ENTER")
    else:
        for i in range(n):
            if not (i in cols) and not (i-nR in d45) and not (i+nR in d135):
                solution[nR] = i

                cols.append(i)
                d45.append(i-nR)
                d135.append(i+nR)

                queens(nR+1, solution, cols, d45, d135)

                cols.pop()
                d45.pop()
                d135.pop()

queens()
