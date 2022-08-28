num, po = map(int,input().split())
temp = po
last = 0
while temp:
    temp-=1
    last=last*10+num%10
    num//=10
rev_last = 0
rev_num = 0
first = 0
while num:
    rev_num=rev_num*10+num%10
    num//=10
while last:
    rev_last=rev_last*10+last%10
    last//=10
while po:
    first=first*10+rev_num%10
    rev_num//=10
    po-=1
if first>rev_last:
    print(first-rev_last)
else:
    print(rev_last-first)