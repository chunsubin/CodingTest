from collections import deque
import sys
n=int(sys.stdin.readline())
numbers=deque([i for i in range(1,n+1)])
cnt=0
while(cnt<n-1):
    numbers.popleft();
    numbers.append(numbers.popleft())
    cnt+=1

print(numbers[0])

