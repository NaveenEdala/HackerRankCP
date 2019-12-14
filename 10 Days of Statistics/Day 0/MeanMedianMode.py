# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy import stats as st
n = int(input())
lol = sorted([int(i) for i in input().split()])
print(sum(lol)/n)
if (n%2==0):
    print((lol[(n-1)//2] + lol[((n-1)//2) + 1])/2)
else:
    print(lol[(n-1)/2])
print(int(st.mode(lol)[0]))
