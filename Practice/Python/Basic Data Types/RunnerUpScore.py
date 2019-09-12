if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

listx = []
for element in arr:
    listx.append(element)
listx.sort(reverse=True)
winner = listx[0]
for i in range(n):
    if winner>listx[i]:
        print(listx[i])
        break
