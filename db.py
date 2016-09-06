import sqlite3 as lite

filename = "tasks.tsdb"


class DBConnect():
    def __init__(self, sqlite_file=None):
        sqlite_file = filename
        self.conn = lite.connect(sqlite_file)
        self.cursor = self.conn.cursor()

    def insert(self, table_name, fields, values):
        sql = "INSERT OR IGNORE INTO {tn} ({flds}) VALUES ({vls})".format(tn=table_name, flds=fields, vls=values)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except lite.Error as e:
            print(e)

    def update(self, table_name, values, condition):
        sql = "UPDATE OR IGNORE {tn} set {vls} where {cond}".format(tn=table_name, vls=values,cond=condition)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except lite.Error as e:
            print(e)

    def delete(self, table_name, condition):
        sql = "DELETE OR IGNORE FROM {tn} where {cond}".format(tn=table_name, cond=condition)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except lite.Error as e:
            print(e)

db=DBConnect()
db.insert("taxas","'nome','valor','modiefied','updated','obs'", "'VAT', 19.00,'16/09/2016','16/09/2016',''")