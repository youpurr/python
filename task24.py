n = int(input('n = '))
lis = [int(x) for x in input('-> ').split()]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max(ma, lis[i] + lis[i+1] + lis[i-1])
print(ma)
