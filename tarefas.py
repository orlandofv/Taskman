# -*- coding: latin-1 -*-
"""
Created on Fri Mar 02 23:18:43 2012

@author: lims
"""
import datetime
import sqlite3 as lite
import random

from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class tarefa(QDialog):
    
    def __init__(self,parent=None):
        super(tarefa,self).__init__(parent)
       
        self.accoes()
        self.ui()
        #self.connectdb()

    def ui(self):
        html = """<center style= "{color:blue;}" > <h2 > Cadastro de Tarefas </h2> </center> """
        validator = QRegExp(r"\d{1,1}")
        
        titulo = QLabel(html)
        cod = QLabel("Codigo")
        tarefa = QLabel("Tipo de Tarefa")
        descricao = QLabel("Descrição de Tarefa")
        cliente = QLabel("Cliente")
        data = QLabel("Data de Execução")
        local = QLabel("Endereço")
        aviso  = QLabel("Avisar antes de:")
        obs = QLabel("Observações")
        
        calendario = QCalendarWidget()
        calendario1 = QCalendarWidget()
        
        self.cod = QLineEdit()
        self.cod.setMaximumWidth(140)
        self.cod.setAlignment(Qt.AlignRight)
        self.cod.setEnabled(False)
        self.tarefa =  QLineEdit()
        self.descricao = QLineEdit()
        self.cliente = QComboBox()
        self.data = QDateTimeEdit()
        self.data.setDate(QDate.currentDate())
        self.data.setObjectName("cal1")
        self.data.setCalendarPopup(True)
        self.data.setCalendarWidget(calendario)
        self.data.setMaximumWidth(140)
        self.data.setAlignment(Qt.AlignRight)
        self.local =  QLineEdit()
        self.aviso  = QDateEdit()
        self.aviso.setDate(QDate.currentDate())
        #self.aviso.setMinimumDate(QDate('1900','01','01'))
        self.aviso.setCalendarPopup(True)
        self.aviso.setCalendarWidget(calendario1)
        self.aviso.setObjectName("cal2")
        self.aviso.setMaximumWidth(140)
        self.aviso.setAlignment(Qt.AlignRight)
        self.obs =QTextEdit()

        grid = QFormLayout()
        
        grid.addRow(cod           ,self.cod              )
        grid.addRow(tarefa          ,self.tarefa             )
        grid.addRow(descricao       ,self.descricao          )
        grid.addRow(data       ,self.data          )
        grid.addRow(aviso      ,self.aviso         )
        grid.addRow(local      ,self.local         )
        grid.addRow(cliente          ,self.cliente             )
        grid.addRow(obs           ,self.obs              )
        
        vLay = QVBoxLayout(self)
        vLay.setContentsMargins(0,0,0,0)
        
        cLay = QVBoxLayout()
        cLay.setContentsMargins(10,10,10,10)
        
        cLay.addLayout(grid)
        
        vLay.addWidget(titulo)
        vLay.addLayout(cLay)
        vLay.addWidget(self.tool)
        self.setLayout(vLay)

        self.setWindowTitle("Cadastro de hospedes")
        
        style = """
            margin: 0;
            padding: 0;
            border-image:url(./images/transferir.jpg) 30 30 stretch;
            background:#303030;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 12px;
            color: #FFFFFF;
        """ 
        
        titulo.setStyleSheet(style)
        
        style2 = """
            QDialog{margin: 0;
        	padding: 0;
            border-image:url(./images/aqua.JPG) 30 30 stretch;
            background:#C0C0CC;
        	font-family: Arial, Helvetica, sans-serif;
        	font-size: 12px;
        	color: #FFFFFF;}
        """

    def accoes(self):
        self.tool = QToolBar(self)
        
        gravar = QAction(QIcon("./images/ok.png"),"&Gravar dados",self)
        eliminar = QAction(QIcon("./images/Delete.ico"),"&Eliminar dados",self)
        
        fechar = QAction(QIcon("./images/filequit.png"),"&Fechar",self)
        
        self.tool.addAction(gravar)
        self.tool.addAction(eliminar)
      
        self.tool.addSeparator()
        self.tool.addAction(fechar)

        self.connect(gravar, SIGNAL("triggered()"), self.addrecord)
        self.connect(eliminar, SIGNAL("triggered()"),self.limpar)
        self.connect(fechar, SIGNAL("triggered()"), self.fechar)
        
#==============================================================================   
        
    def fechar(self):
        self.close()
    
    def limpar(self):
        for child in (self.findChildren(QLineEdit) or self.findChildren(QTextEdit)):
            if child.objectName() not in ["cod","cal1","cal2"]: child.clear()
                
    def connectdb(self):

        self.conn = lite.connect('./db/maindb.db')
        self.cursor = self.conn.cursor()
        self.incrementa()
        self.conn.commit()
    
    def validacao(self):

        if str(self.tarefa.text()) == "":
            QMessageBox.warning(self,"Erro", "Entre o nome da Tarefa")
            self.tarefa.setFocus()
            return False
        elif self.descricao.text() == "":
            QMessageBox.warning(self, "Erro", "Entre a descrição da tarefa da Tarefa")
            self.descricao.setFocus()
            return False
        elif self.data.date() <= QDate.currentDate():
            QMessageBox.warning(self,"Erro", "Data de data de ser menor ou igual a data actual.")
            self.data.setFocus()
            return False
        elif self.aviso.date() >= self.data.date():
            QMessageBox.warning(self,"Erro", "A data de aviso deve ser menor que a data da Tarefa.")
            self.aviso.setFocus()
            return False
        else:
            return True

    def mostrarReg(self,cod):
        sql = str("select * from hospedes where cod = %s" %cod)
        self.cursor.execute(sql)
        
        dados = self.cursor.fetchall()
        for item in dados:
            
            self.tarefa.setText(item[1])
            self.endereco.setText(item[2])
            self.cliente.setCurrentIndex(self.cliente.findText(item[3]))
            self.nacionalidade.setCurrentIndex(self.nacionalidade.findText(item[4]))
            self.tipo.setCurrentIndex(self.tipo.findText(item[5]))
            self.numero.setText(item[6])
            self.data.setDateTime(QDateTime.fromString(item[7]))
            self.aviso.setDate(QDate.fromString(item[8]))
            self.emergencia.setText(item[9])
            self.descricao.setText(item[10])
            self.contacto.setText(item[11])
            self.email.setText(item[12])
            self.obs.setPlainText(item[13]) 

    def addrecord(self):

        if self.validacao() == True:
            cod = self.cod.text()
            tarefa = self.tarefa.text()
            descricao = self.descricao.text()
            endereco = self.endereco.text()
            cliente = self.cliente.currentText()
            email = self.email.text()
            data = QDateTime(self.data.dateTime()).toString()
            contacto = self.contacto.text()
            emergencia = self.emergencia.text()
            tipo = self.tipo.currentText()
            numero = self.numero.text()
            nacionalidade = self.nacionalidade.currentText()
            aviso  = QDate(self.aviso.date()).toString()
            obs = self.obs.toPlainText() 
            func1 = "orlando"
            func2 = "orlando"
            estado  ="ocupado"

            if self.parent().actualizar == True:
                sql = """update hospedes set tarefa = "%s" , endereco = "%s"
                ,cliente = "%s" , nacionalidade = "%s" ,tipo_id ="%s" 
                , numero_id = "%s", data = "%s" ,  aviso_id = "%s" ,
                emergencia = "%s", descricao = "%s", contactos = "%s" ,email = "%s"
                , obs ="%s" ,estado = "%s" , func1 = "%s",data = data ,
                func2 = "%s" , data2 = "%s"  where cod = "%s" """ \
                % (tarefa,endereco,cliente,nacionalidade,tipo,numero,data,
                aviso,emergencia,descricao,contacto,email,obs,estado,func1, 
                func2,QDate.currentDate().toString(),self.parent().numeroHospede)
            else:
                sql = """INSERT INTO hospedes values (
                "%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s", "%s" ,"%s" ,"%s" ,
                "%s","%s" ,"%s"  ,"%s" ,"%s" ,"%s","%s" ,"%s" ,"%s" )""" % (cod,
                tarefa,endereco,cliente,nacionalidade,tipo,numero,data,aviso,
                emergencia,descricao,contacto,email,obs,estado,func1,
                QDate.currentDate().toString(),func2,QDate.currentDate().toString())
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                #messagem = QMessageBox.information(self,"Informação","Registro Gravado com sucesso!",QMessageBox.Ok)
                
                if QMessageBox.question(self,"Pergunta","Registo Gravado com sucesso!\nDeseja Cadastrar outro Item?",
                               QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
                    self.parent().actualizar = False                
                    self.incrementa()
                else:
                    self.close()
                
            except lite.Error as e:
                erro =  "Erro: %s . Reporte ao suporte." % e
                messagem = QMessageBox.critical(self,"Erro","Dados não gravados." + erro ,QMessageBox.Ok)
                return

    def closeEvent(self,evt):
        parente =  self.parent()
        parente.encheTabela()
        self.conn.close()


