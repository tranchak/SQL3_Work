import psycopg2

conn = psycopg2.connect(dbname='lessondb', user='dima',
                        password='95462037', host='localhost')
cursor = conn.cursor()
sql = """CREATE TABLE less1
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(30),
    LastName CHARACTER VARYING (30),
    Email CHARACTER VARYING (30),
    Age INTEGER );"""

cursor.execute(sql)
conn.commit()
conn.close()
