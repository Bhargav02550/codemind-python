s = input()
r = ""
a = "qwertyuiopalskdjfhgmznxbcvQWERTYUIOPALSKDJFHGMZNXBCV"
for i in s:
    if i in a:
        r+=i
r = list(r)
r = r[::-1]
r = ''.join(r)
ans = ''
j=0
for i in range(len(s)):
    if s[i] in a:
        ans+=r[j]
        j+=1
    else:
        ans+=s[i]
print(ans)