import sys
a,b,v = map(int,sys.stdin.readline().split())

tmp = (v-a)/(a-b)+1
if tmp>int(tmp):
    tmp+=1

print(int(tmp))