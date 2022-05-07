l=int(input())
n=int(input())
for i in range(1,n+1):
    w,h=map(int,input().split())
    if(w<l or h<l):
        print("UPLOAD ANOTHER")
    elif w==l and h==l or w==h:
        print("ACCEPTED")
    else:
        print("CROP IT")