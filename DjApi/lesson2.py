import sqlite3 #внесение записей в базу данных

conn = sqlite3.connect('db.sqlite3') #cоздает соединение с БД.
cursor = conn.cursor() #подготовка запроса с SQL ставим курсор для работы
SQL ='''INSERT INTO main_auto ('id', 'name', 'price', 'brand_id')
        VALUES (6, 'ET', 105, 2)
'''
c=cursor.execute(SQL) #Выполнить запрос по SQL
conn.commit()
conn.close()

# SELECT name as x, price as y FROM main_auto