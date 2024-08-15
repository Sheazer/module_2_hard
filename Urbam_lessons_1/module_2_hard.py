a = int(input())
s = ''
for i in range(1, int(a/2)+1):
    if a % i == 0:
        for j in range(i-1, int(i/2), -1):
            s+= str(i-j) + str(j)
for i in range(a-1, int(a/2), -1):
    s+= str(a-i) + str(i)
print(s)