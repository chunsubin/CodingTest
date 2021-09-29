import sys
q = []
n=int(sys.stdin.readline())
for i in range(n):
    inp = sys.stdin.readline().split()
    if inp[0]=="push":
        q.append(inp[1])
    elif inp[0]=="pop":
        if len(q)==0:print(-1)
        else:
            print(q[0])
            q=q[1:]
    elif inp[0]=="size":
        print(len(q))
    elif inp[0]=="empty":
        if len(q)==0: print(1)
        elif len(q)>0: print(0)
    elif inp[0]=="front":
        if len(q)==0:print(-1)
        else: print(q[0])
    else:
        if len(q)==0:print(-1)
        else: print(q[-1])