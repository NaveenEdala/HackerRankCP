# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(n))
