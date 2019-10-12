if __name__ == '__main__':
    dataset = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        dataset.append([name, score])

dataset.sort(key=lambda databit: (databit[1], databit[0]))

runnerup = [databit[1] for databit in dataset if databit[1] != dataset[0][1]][0]

for i in [databit for databit in dataset if databit[1]==runnerup]:
    print(i[0])
