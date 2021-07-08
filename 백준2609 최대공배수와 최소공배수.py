import sys
a,b = map(int,sys.stdin.readline().split())
for i in range(max(a,b),0,-1):
    if a%i==0 and b%i==0:
        a/=i
        b/=i
        break

print(i)
print(int(i*a*b))