import csv


with open('books.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=';'))[1:]

    for i in range(1, len(data)):
        j = i - 1
        ch1 = int(data[j + 1][-1][0])
        ch2 = int(data[j][-1][0])
        if j >= 0 and ch1 < ch2:
            data[j + 1], data[j] = data[j], data[j + 1]
