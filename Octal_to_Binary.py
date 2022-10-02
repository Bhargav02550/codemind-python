def OctToBin(o):
    return bin(int(o,8))
for i in range(int(input())):
    onum = input()
    bnum = OctToBin(onum)
    print(bnum[2:])