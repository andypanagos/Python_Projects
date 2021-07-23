
import sqlite3


def Create_Table():
    # Creating database
    conn = sqlite3.connect('assignment.db')
    with conn:
        cur = conn.cursor()
    # Creating table
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_for_database_assignment( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_file_list TEXT \
                )")
        conn.commit()
    conn.close()


def File_List():
    # File names to look through
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    for var1 in fileList:
        # Finding files ending with ".txt"
        if var1.endswith('.txt'):
            conn = sqlite3.connect('assignment.db')
            # Inserting file names into table in database
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_for_database_assignment(col_file_list) VALUES (?)", (var1,))
                conn.commit()
            conn.close()


if __name__ == "__main__":
    Create_Table()
    File_List()
