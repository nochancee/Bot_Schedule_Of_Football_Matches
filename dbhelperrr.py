import sqlite3


class DBHelper:
    def __init__(self, dbname="clubs.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text, owner):
        stmt = "INSERT INTO items (description, owner) VALUES (?, ?)"
        args = (item_text, owner )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, owner):
        cursor = self.conn.cursor()
        user_id = str(owner)
        sqlite_update_query = """DELETE from items where owner = ?"""
        cursor.execute(sqlite_update_query, (user_id,))
        self.conn.commit()
        cursor.close()

    def get_items(self, owner):
        cursor = self.conn.cursor()
        user_id = owner
        sqlite_select_query = """SELECT * from items"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        clubs = []
        for row in records:
            if str(row[1]) == str(user_id):
                clubs.append(row[0])
        cursor.close()
        return(clubs)