# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
inputs = input().strip().split()
if len(set(inputs)) == len(inputs):
    print("YES")
else:
    print("NO")
