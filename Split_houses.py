sample = int(input())
string = input() 
flag = string.find("HH") 
if flag == -1:
    print("YES") 
    print(string.replace(".","B")) 
else:
    print("NO")