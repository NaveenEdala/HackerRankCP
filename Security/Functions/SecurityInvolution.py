# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split()))

for i in range(0,n):
    if (i+1 != arr[arr[i]-1]):
        print('NO')
        exit(0)
print('YES')
