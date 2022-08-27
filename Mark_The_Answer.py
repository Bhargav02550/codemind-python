N, X = map(int,input().split())
A=list(map(int,input().split()))
score = 0
skip = 0
for i in A:
    if skip > 1:
        break
    else:
        if i > X:
            skip +=1
        else:
            score +=1
print(score)