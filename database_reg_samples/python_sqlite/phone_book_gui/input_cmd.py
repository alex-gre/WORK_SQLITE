# Импорт библиотеки
import sqlite3
 
conn = sqlite3.connect("TELBOOK.db")
cursor = conn.cursor()
    # Создание таблицы
cursor.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY,\
                              First TEXT, Surname TEXT,Tel TEXT,info TEXT)")
conn.commit()
     # Вводим данные
First = input('Введите Имя: ')
Surname = input('Фамилия: ')
Tel = input('Телефон: ')
info = input('Информация: ')

    # Вставляем данные в таблицу
cursor.execute('''INSERT INTO profile(First,Surname,Tel,info) VALUES (?, ?, ?,?)''', (First,Surname,Tel,info))
conn.commit()
    # Сохраняем изменения
conn.commit()
cursor.close()
conn.close()
