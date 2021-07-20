
import sqlite3


conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_cities(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_city_name TEXT \
        )")
    conn.commit()
conn.close()




conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_cities(col_city_name) VALUES (?)", \
                ('New York City'))
    cur.execute("INSERT INTO tbl_cities(col_city_name) VALUES (?)", \
                ('Los Angeles'))
    cur.execute("INSERT INTO tbl_cities(col_city_name) VALUES (?)", \
                ('Chicago'))
    cur.execute("INSERT INTO tbl_cities(col_city_name) VALUES (?)", \
                ('Houston'))
    cur.execute("INSERT INTO tbl_cities(col_city_name) VALUES (?)", \
                ('Phoenix'))
    conn.commit()
conn.close()
