from PyQt4 import QtSql, QtGui
from PyQt4.QtSql import QSqlDatabase
from PyQt4.QtSql import QSqlQuery

filename = 'tasks.tsdb'

class DBCOnnection(QSqlDatabase):

    def __init__(self, file=None):

        super(DBCOnnection, self).__init__(file)
        file= filename
        self.db = self.addDatabase('QSQLITE')
        self.db.setDatabaseName(file)

        if not self.db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                     "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it.\n\n" "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)
            return

    def insert(self, table_name,fields, values):
        sql = "INSERT OR IGNORE INTO {tn} ({flds}) VALUES ({vls})".format(tn=table_name, flds=fields,vls=values)

        query = QSqlQuery()
        query.exec_(sql)

    def insert(self, table_name, values):
        sql = "INSERT OR IGNORE INTO {tn} VALUES ({vls})".format(tn=table_name, vls=values)


        query = QSqlQuery()
        query.exec_(sql)

    def update(self, table_name, values, condition):
        sql = "UPDATE OR IGNORE {tn} set {vls} where {cond}".format(tn=table_name, vls=values, cond=condition)

        query = QSqlQuery()

        try:
           query.exec_(sql)
        except query.lastError() as e:
            print(e)

    def delete(self, table_name, condition):
        sql = "DELETE OR IGNORE FROM {tn} where {cond}".format(tn=table_name, cond=condition)

        query = QSqlQuery()

        try:
            query.exec_(sql)
        except query.lastError() as e:
            print(e)
#
# values = "CL2016961SRP" ,"ORLANDO FILIPE" ,"MAVALANE" ,"Masculino" ,"África do Sul" ,"BI" ,"1122345678M", "Tue Sep 6 00:00:00 2016" ,"Tue Sep 6 2016" ,"870112233" ,\
#          "VILANCULO", "860112233" , "vilankazi@gmail.com"  , "" , "ocupado" ,"orlando","Tue Sep 6 2016" ,"orlando" ,"Tue Sep 6 2016"
#
#
# if __name__ == '__main__':
#      import sys
#      app = QtGui.QApplication(sys.argv)
#      db = DBCOnnection(filename)
#      db.insert("clientes",values)