import sys
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    cnt=0
    lis = list(map(int,sys.stdin.readline().split()))
    ave = sum(lis[1:])/lis[0]
    for j in (lis[1:]):
        if ave<j: cnt+=1

    result = '%.3f'%((cnt/lis[0])*100)
    print(str(result)+"%")