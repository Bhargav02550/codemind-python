str=input("")
arr=[0]*256
max=0
sec_max=0
i=0
for i in range(len(str)):
    if str[i]!=' ':
        num=ord(str[i])
        arr[num]+=1
for i in range(256):
    if arr[i] > arr[max]:
        sec_max = max
        max = i
    elif arr[i]>arr[sec_max] and arr[i]!=arr[max]:
        sec_max = i
if(sec_max==0):
    print("-1")
else:
    print((chr)(sec_max))