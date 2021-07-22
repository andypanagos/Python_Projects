
import sqlite3

# Creating database
conn = sqlite3.connect('db_assignment.db')

with conn:
    cur = conn.cursor()
    
    # Creating table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_for_database_assignment( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_list TEXT \
        )")
    
    # Inserting values into table
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", \
                ('myPhoto.jpg',))

    #Printing file names ending in '.txt'
    cur.execute("SELECT col_file_list FROM tbl_for_database_assignment WHERE col_file_list LIKE '%.txt'")
    row = cur.fetchall()
    print(row)
    conn.commit()
conn.close()






