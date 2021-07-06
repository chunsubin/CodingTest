import sys

def binary_search(target, start, end, data):
    if start>end:
        return 0

    mid = (start + end)//2

    if data[mid]==target:
        return 1
    elif data[mid]>target:
        end= mid-1
    else:
        start=mid+1

    return binary_search(target, start, end, data)

n=sys.stdin.readline()
arr1 = list(map(int, sys.stdin.readline().split()))
m=sys.stdin.readline()
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()

for i in arr2:
    print(binary_search(i,0,int(n)-1,arr1))