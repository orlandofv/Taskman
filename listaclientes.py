# -*- coding: latin-1 -*-
"""
Created on Fri Sep 13 11:46:33 2013

@author: itbl_orlando
"""

#!/usr/bin/env python

#import psycopg2
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3 as lite
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt4.QtWebKit import *


class Listaclientes(QMainWindow):


    def __init__(self, parent=None):
        super(Listaclientes, self).__init__(parent)
        
        self.actualizar = False    
        self.numeroCliente = ""
        self.totalItems = 0
        self.pai = "cliente"
        self.filho = False
        self.nomeCliente = ""
        
        self.tabela =  QTableView()
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSortingEnabled(True)
        self.tabela.setAlternatingRowColors(True)
        # hide grid
        self.tabela.setShowGrid(False)

        # set the font
        font = QFont("Courier New", 10)
        self.tabela.setFont(font)

        # hide vertical header
        vh = self.tabela.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = self.tabela.horizontalHeader()
        hh.setStretchLastSection(True)

        # set column width to fit contents
        self.tabela.resizeColumnsToContents()
        
        self.setCentralWidget(self.tabela)
        
        self.db = self.parent().db
        
        self.toolbar()
        self.encheTabela()
        self.setWindowTitle("Lista de Hóspedes")
        
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
        
        self.addToolBarBreak(Qt.BottomToolBarArea)
        self.addToolBar(tool)
        
        
        ######################################################################
        self.connect(novo,SIGNAL("triggered()"),self.novoCliente)
        self.connect(self.procura,SIGNAL("textEdited(QString)"), self.encheTabela)
        self.tabela.clicked.connect(self.clickedSlot)
        self.tabela.doubleClicked.connect(self.selecionarDados)
        self.connect(apagar,SIGNAL("triggered()"),self.apagarLinha)
        self.connect(actualizar,SIGNAL("triggered()"),self.actualizarDados)
        imprimir.triggered.connect(self.imprime)

    def imprime(self):

        import sqlite3 as lite
        from html import HTML

        footer = """
        <footer>
          <p>Posted by: Hege Refsnes</p>
          <p>Contact information: <a href="mailto:someone@example.com">
          someone@example.com</a>.</p>
        </footer>
        """
        conn = lite.connect("./db/maindb.db")
        conn.text_factory(str)
        cursor = conn.cursor()

        sql = str( "select (nome || ' ' || apelido ) ,email" \
              ",contactos,emergencia ,nacionalidade" \
              ",obs  from clientes where nome like '%" + self.procura.text()  \
              + "%' or nacionalidade like '%" + str(self.procura.text())  + "%' order by cod")

        cursor.execute(sql)
        dados = cursor.fetchall()

        if len(dados) == 0: return

        setings = QSettings()
        empresa= setings.value("empresa/nome")
        cabecalho = setings.value("empresa/cabecalho")
        logotipo = setings.value("empresa/logo")

        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)

        html = "<img src = %s >" % logotipo
        html += "<p> <bold> %s </bold> </p>" % empresa
        html += "<p> %s </p>" % cabecalho
        html += "<center> <h1> Lista de clientes </h1> </center>"
        html += "<hr/>"
        html += "<br/>"
        html += "<table>"

        html += "<tr style='background:#8C8C8C;'>"
        html += "<th>Nome</th>"
        html += "<th>Email</th>"
        html += "<th>Contactos</th>"
        html += "<th>Emargencia</th>"
        html += "<th>Nacionalidade</th>"
        html += "<th>Notas</th>"
        html += "</tr>"

        for cliente in dados:
            html += ("""<tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr>""") % \
                    (cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5])
        html += "</table>"
        html += footer

        document = QTextDocument() #QWebView()

        document.setHtml(html)

        dlg = QPrintPreviewDialog(self)
        dlg.paintRequested.connect(document.print_)
        dlg.showMaximized()

        dlg.exec_()

    def selecionarDados(self,widget):
        if self.filho ==True :
            if self.pai == "cliente":
                self.parent().cliente.setText(self.nomeCliente)
                self.close()
        else:
            self.actualizarDados()
            
    def focusInEvent(self,evt):
        self.encheTabela()
    
    def actualizarDados(self):
        
        self.actualizar = True
        
        import clientes
        
        qrt =  clientes.Cliente(self)
        qrt.setModal(True)
        qrt.show()

    def barradeEstado(self):
        estado = QStatusBar(self)
        
        items = QLabel("Total de clientes: %s" % self.totalItems)
        seleccionado = QLabel("Cliente seleccionado: %s" % self.numeroCliente)
        estado.addWidget(items)
        estado.addWidget(seleccionado)
        
        self.setStatusBar(estado)
        
    def novoCliente(self):
        
        self.actualizar = False
        
        import clientes
        from utilities import codigo
        
        qrt =  clientes.Cliente(self)
        qrt.cod.setText("CL" + codigo("PQRSTUVXYWZ0123456789"))
        qrt.setModal(True)
        qrt.show()
        
    def printTable(self,printer,painter,area):
        model = self.modelo
        myTableView = self.tabela
        printer = painter #self.myprinter
        rows = model.rowCount();
        columns = model.columnCount();
        totalWidth = 0.0;
        totalPageHeight = 0.0;
        totalHeight = 0.0;
        for c in range(columns):
            totalWidth += myTableView.columnWidth(c)
        
        
        for p in range(45):
            totalPageHeight += myTableView.rowHeight(p);
    
        for r in range(rows):
            totalHeight += myTableView.rowHeight(r);
    
        xscale = area.width() / totalWidth;
        yscale = area.height() / totalHeight;
        pscale = area.height() / totalPageHeight;
        painter.scale(xscale, pscale);
        painter.translate(area.x() + xscale, area.y() + yscale);
    
        x=0
        #QStyleOptionViewItem option;
    
        for r in range(rows):
            ++x
            for c in range(columns):
                idx = model.index(r,c);
                option = myTableView.viewOptions();
                option.rect = myTableView.visualRect(idx);
                if r % 2 == 0:
                    brush= QtGui.QBrush(QtGui.QColor(220, 220, 220), QtCore.Qt.SolidPattern);
                    painter.fillRect(option.rect, brush);
                myTableView.itemDelegate().paint(painter, option, idx);
    
            if (x == 45):
                ok = printer.newPage();
                x=0;
                painter.translate(0, -1350);
            
    def encheTabela(self):

        if self.filho:
            sql = "select cod as [Código],(nome || ' ' || apelido ) as [Nome],email as [Email]" \
                  ",contactos as Contactos,emergencia as [No de Emergência] ,nacionalidade as [Nacionalidade]" \
                  ",obs as [Observações] from clientes where nome like '%" + self.procura.text()  \
                  + "%' or nacionalidade like '%" + str(self.procura.text()) + "%' order by cod"
        else:
            sql = "select cod as [Código],(nome || ' ' || apelido ) as [Nome],email as [Email]" \
                  ",contactos as Contactos,emergencia as [No de Emergência] ,nacionalidade as [Nacionalidade]" \
                  ",obs as [Observações] from clientes where nome like '%" + self.procura.text()  \
                  + "%' or nacionalidade like '%" + str(self.procura.text())  + "%' order by cod"


        self.modelo = QSqlQueryModel()
        self.modelo.setQuery(sql, self.db)
        self.totalItems = self.modelo.rowCount()
       
        self.tabela.setModel(self.modelo)

        self.barradeEstado()
        
    def showEvent(self,evt):
        self.encheTabela()
    
    def closeEvent(self,evt):
        if self.filho == True: self.parent().mclientes = False
        
        
    def clickedSlot(self,index):
        
        self.coluna = str(index.column())
        self.linha =   str(index.row())
        
        item = self.modelo.record(int(self.linha)).value(1)
        item2 = self.modelo.record(int(self.linha)).value(0)
        self.numeroCliente = str(item2)
        self.nomeCliente = str(item)
        self.barradeEstado()
        
    def apagarLinha(self):
        
        if self.numeroCliente == "": return
        
        sql = "delete from clientes where cod = '%s'" % self.numeroCliente
       
        if QMessageBox.question(self,"Pergunta",str("Deseja Apagar o Cliente número %s?") % self.numeroCliente,
                                QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
           
           self.modelo.setQuery(sql)
           self.encheTabela()
           QMessageBox.information(self,"Sucesso","Item apagado com sucesso...")
           
#            con = lite.connect("./db/maindb.db")
#            cursor = con.cursor()
#            cursor.execute(sql)
#            con.commit()
#            con.close()
            
            
            
            
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    wnd = listaCliente()
#    wnd.resize(640, 480)
#    wnd.show()
#    sys.exit(app.exec_())