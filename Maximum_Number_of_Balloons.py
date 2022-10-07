s = input()
b = s.count('b')
a = s.count('a')
l = s.count('l')
o = s.count('o')
n = s.count('n')
c = 0
l = l//2
o = o//2
while b!=0 and a!=0 and n!=0 and l!=0 and o!=0:
    c+=1
    b-=1
    a-=1
    n-=1
    l-=1
    o-=1
print(c)