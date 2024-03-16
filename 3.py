import csv

# функция для поиска подходящего автора с его книгой
def search(iid, data):
    for stroka in data:
        if iid in stroka[2]:
            return stroka


with open('books.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=';'))[1:]


    #  поиск ведётся по автору!!!
    iid = input()
    while iid != 'хватит':
        s = []
        r = search(iid, data)
        if iid == '':
            print('Данного автора в этой библиотеке нет')
        elif r != None:
            print(f'Название книги: {r[-2]} - {r[1]} - {r[0]} - {r[-1]}')
        else:
            print('Данного автора в этой библиотеке нет')

        iid = input()