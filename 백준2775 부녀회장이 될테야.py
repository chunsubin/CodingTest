import sys
n = int(sys.stdin.readline())
for i in range(n):
    people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    k=int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for j in range(k):
        for k in range(1,n):
            people[k]+=people[k-1]

    #print(people)
    print(people[n-1])