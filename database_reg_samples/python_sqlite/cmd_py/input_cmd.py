# Импорт библиотеки
import sqlite3
 
conn = sqlite3.connect("patient.db")
cursor = conn.cursor()
    # Создание таблицы
cursor.execute(
    'CREATE TABLE IF NOT EXISTS pat (fio TEXT, adr TEXT, birth INTEGER,region TEXT,diagnos TEXT)')
conn.commit()
     # Вводим данные
fio = input('Введите ФИО: ')
adr = input('Адрес прописки: ')
birth = input('Дата рождения: ')
region = input('Область: ')
diagnos=input('Диагноз: ')
    # Вставляем данные в таблицу
cursor.execute('''INSERT INTO pat(fio, adr, birth, region,diagnos) VALUES (?, ?, ?, ?,?)''', (fio, adr, birth, region,diagnos))
conn.commit()
    # Сохраняем изменения
conn.commit()
cursor.close()
conn.close()
