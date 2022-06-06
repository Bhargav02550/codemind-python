n=int(input())
l=len(str(n))
s=n**2
au=s%pow(10,l)
if au==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")