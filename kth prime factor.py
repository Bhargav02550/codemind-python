a=int(input())
b=int(input())
prime=[1]*(a+1)
prime[0]=prime[1]=0
for i in range(2,a+1):
    if prime[i]==1:
        for j in range(i+i,a+1,i):
            prime[j]=0
pfac = []
cop = a
for i in range(2,a+1):
    if prime[i]==1:
        while cop%i==0:
            pfac.append(i)
            cop//=i
if len(pfac)<b:
    print(-1)
else:
    print(pfac[b-1])
