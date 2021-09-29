import sys
n=int(sys.stdin.readline())
b5 = n//5
r = n%5
b3=0

if r==0:
    print(b5)
elif r==1 and b5>=1:  # 5봉지하나 줄이기
    b5-=1
    b3+=2
    print(b5+b3)
elif r==2 and b5>=2:
    b5-=2
    b3+=4
    print(b5 + b3)
elif r==3:
    b3+=1
    print(b5 + b3)
elif r==4 and b5>=1:
    b5-=1
    b3+=3
    print(b5 + b3)
else:
    print(-1)
