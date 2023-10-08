t=int(input())
l=[2,3,5,7,9,11,13,19,23,29,31,37,41,47,51]
for i in range(t):
    c=1
    m=0
    n=int(input())
    for i in l:
        c*=i
        if c<n:
            m+=1
        elif c==n:
            m+=1
            break
        else:
            break
    print(m)
