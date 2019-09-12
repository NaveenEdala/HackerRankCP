if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

total = 0
average = 0
j = 0
for scores in student_marks[query_name]:
    total+=scores
    j += 1
average = total / j
print("%.2f" % average)
