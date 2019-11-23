# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = list(map(int,input().split()))
for i in range(1,n+1):
    print(s.index(i)+1)
