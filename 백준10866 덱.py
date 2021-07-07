import sys
from collections import deque
d=deque()
n=int(sys.stdin.readline())

for i in range(n):
    inp=sys.stdin.readline().split()
    if inp[0]=="push_front":
        d.appendleft(inp[1])
    elif inp[0]=="push_back":
        d.append(inp[1])
    elif inp[0] == "pop_front":
        if d.__len__() == 0: print(-1)
        else:print(d.popleft())
    elif inp[0] == "pop_back":
        if d.__len__() == 0: print(-1)
        else: print(d.pop())
    elif inp[0] == "size":
        print(d.__len__())
    elif inp[0] == "empty":
        if d.__len__()==0: print(1)
        else: print(0)
    elif inp[0] == "front":
        if d.__len__()==0: print(-1)
        else: print(d[0])
    elif inp[0] == "back":
        if d.__len__()==0: print(-1)
        else: print(d[-1])

print(d)