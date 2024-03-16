import csv

# Открываем файл со списком книг и создаём ещё новый файл
with open('books.csv', encoding='utf-8') as file, open('books_rowling.csv', 'w', encoding='utf-8', newline='') as new_file:
    data = list(csv.reader(file, delimiter=';'))
    res = csv.writer(new_file,  delimiter=';')


    # Делаем шапку таблицы
    data_1 = []
    data_1.append('Author')
    data_1.append('original_title')
    data_1.append('ratings_1')
    res.writerow(data_1)


    #вставляем значения в таблицу (используя условия по рейтингу, по автору и по самой книги
    for stroka in data[1:]:
        if int(stroka[-1][0]) >= 8 and int(stroka[-1][2:]) > 0 and 'Дж.К. Роулинг' in stroka[2]:
            data_2 = []

            data_2.append(stroka[2])
            data_2.append(stroka[4])
            data_2.append(stroka[-1])
            res.writerow(data_2)
