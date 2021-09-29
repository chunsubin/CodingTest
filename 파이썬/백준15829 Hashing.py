n=int(input())
alpha=["0","a","b","c","d","e","f","g","h","i","j",
       "k","l","m","n","o","p","q","r","s","t",
       "u","v","w","x","y","z",]
x=input()
s=0
cnt=0
for i in x:
    s+=alpha.index(i)*31**cnt
    cnt+=1
    if cnt == n:break

print(s)
