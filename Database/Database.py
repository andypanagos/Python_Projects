
import sqlite3


conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_for_database_assignment(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_random_string TEXT \
        )")
    conn.commit()
conn.close()




conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_for_database_assignment(col_random_string) VALUES (?)", \
                ('New York City'))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_random_string) VALUES (?)", \
                ('Basketball'))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_random_string) VALUES (?)", \
                ('Fence'))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_random_string) VALUES (?)", \
                ('Street'))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_random_string) VALUES (?)", \
                ('Sign'))
    conn.commit()
conn.close()



# return all files as a list
for file in os.listdir(r'D:\GFG'):
     # check the files which are end with specific extention
    if file.endswith(".png"):
        # print path name of selected files
        print(os.path.join(r'C:\GFG\Screenshots', file))
