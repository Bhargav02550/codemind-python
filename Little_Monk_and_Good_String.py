arr = input()
count = 0
c = 0
for i in range(0,len(arr)):
    if arr[i]=='a' or arr[i]=='e' or arr[i]=='i' or arr[i]=='o' or arr[i]=='u':
        c+=1
    else:
        if count<c:
            count = c
        c = 0
if count<c:
    count = c
print(count)