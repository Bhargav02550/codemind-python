string = input()
l = len(string)
c = 1
count = 0
for i in range(0,l-1):
    if string[i]==string[i+1]:
        c+=1
    else:
        if count<c:
            count=c
        c = 1
if count<c:
    count=c
print(count)