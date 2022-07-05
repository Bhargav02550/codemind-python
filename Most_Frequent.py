from collections import Counter
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]
n=int(input())
a=list(map(int,input().split()))
print(most_frequent(a))