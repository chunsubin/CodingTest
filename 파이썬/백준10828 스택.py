import sys
s=[]
n=int(sys.stdin.readline())
for i in range(n):
    inp = sys.stdin.readline().split()
    if inp[0]=="push":
        s.append(inp[1])
    elif inp[0]=="pop":
        if len(s)==0:print(-1)
        else:
            print(s[-1])
            s=s[:-1]
    elif inp[0]=="size":
        print(len(s))
    elif inp[0]=="empty":
        if len(s)==0: print(1)
        elif len(s)>0: print(0)
    elif inp[0]=="top":
        if len(s)==0:print(-1)
        else:print(s[-1])


