class Solution:
    def moveRobots (self, s1, s2):
        b=[]
        a=[]
        b1=[]
        a1=[]
        s11=''
        s22=''
        n=len(s1)
        for i in range(n):
            if s1[i]=='A':
                a.append(i)
                s11+='A'
            if s1[i]=='B':
                b.append(i)
                s11+='B'
        for i in range(n):
            if s2[i]=='A':
                a1.append(i)
                s22+='A'
            if s2[i]=='B':
                b1.append(i)
                s22+='B'
        if s11!=s22:
            return 'No'
        for i in range(len(a)):
            if a1[i]>a[i]:
                return "No"
        for i in range(len(b)):
            if b1[i]<b[i]:
                return "No"
        return "Yes"
s1=input()
s2=input()
ob=Solution()
print(ob.moveRobots(s1,s2))