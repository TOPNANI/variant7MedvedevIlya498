import csv


with open('books.csv', encoding='utf-8') as file, open('books_grade.csv', 'w', encoding='utf-8') as new_file:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_file, delimiter=';')
