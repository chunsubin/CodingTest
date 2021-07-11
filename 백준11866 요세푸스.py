from collections import deque
n,k = map(int,input().split())
numbers = deque([i for i in range(1,n+1)])
cnt=0
result="<"
for i in range(n*k):
    cnt += 1
    if cnt==k:
        tmp=numbers.popleft()
        result+=str(tmp)+", "
        cnt=0
    else:
        tmp = numbers.popleft()
        numbers.append(tmp)

result=result[:-2]
result+=">"
print(result)