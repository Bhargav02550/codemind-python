def findFirstAndLast(arr, n, x) :
    first = -1
    last = -1
    for i in range(0, n) :
        if (x != arr[i]) :
            continue
        if (first == -1) :
            first = i
        last = i
     
    if (first != -1) :
        print(first,last)
    else :
        print("-1 -1")
n=int(input())
a=list(map(int,input().split()))
x =int(input())
findFirstAndLast(a,n,x)