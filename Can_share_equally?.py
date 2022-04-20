x,y=map(int,input().split())
if x == 0 and y % 2 != 0:
        print("NO")
elif ((x*1) + (y*2)) % 2 == 0:
        print("YES")
else:
        print("NO")