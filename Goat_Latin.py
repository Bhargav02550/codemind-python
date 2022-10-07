def toGoatLatin(S):
        words = S.split()
        vowels = set("AEIOUaeiou")
        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i] = words[i] + "ma" + "a"*(i+1)
            else:
                words[i] = words[i][1:] + words[i][0] + "ma" + "a"*(i+1)
                
        return " ".join(words)
n=input()
print(toGoatLatin(n))