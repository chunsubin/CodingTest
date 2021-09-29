n=int(input())
numbers=[0]*(n+1)
length = len(str(n))

for i in range(max(0,n-9*length),n+1):
    tmp=i
    numbers[i]+=i
    while(1):
        if tmp==0 : break
        numbers[i]+=int(tmp%10)
        tmp=tmp/10

try:
    print(str(numbers.index(n)))
except ValueError:
    print(0)