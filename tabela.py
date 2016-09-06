# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:46:33 2013

@author: itbl_orlando
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import psycopg2
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3 as lite
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery

con = None
 
class MainWindow(QMainWindow):
 
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.table_widget =  QTableView()
        self.table_widget.setSortingEnabled(True)
        
        layout = QVBoxLayout()
        self.setCentralWidget(self.table_widget)
        self.setLayout(layout)
        #self.populate("hospedes")
        self.toolbar()
        
    def toolbar(self):
        procura = QLabel("Pesquisar:")
        self.procura = QLineEdit(self)
        self.procura.setMaximumWidth(200)
        
        
        novo= QAction(QIcon('./images/add.png'),"Novo",self)
        apagar = QAction(QIcon('./images/editdelete.png'),"Apagar",self)
        imprimir =  QAction(QIcon('./images/fileprint.png'),"Imprimir",self)
        actualizar = QAction(QIcon('./images/pencil.png'),"Actualizar dados",self)

        tool = QToolBar()

        tool.addWidget(procura)
        tool.addWidget(self.procura)
        tool.addSeparator()
        tool.addAction(novo)
        tool.addAction(actualizar)
        tool.addSeparator()
        tool.addAction(apagar)
        tool.addSeparator()
        tool.addAction(imprimir)

        tool.setAllowedAreas(Qt.BottomToolBarArea)
        self.addToolBar(tool)

    def populate(self,table=None):

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("./db/maindb.db")
        db.open()

        sql = ("select * from %s" %table)
        projectModel = QSqlQueryModel()
        projectModel.setQuery(sql,db)
        self.table_widget.setModel(projectModel)
 
