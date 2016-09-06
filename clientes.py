# -*- coding: latin-1 -*-
"""
Created on Fri Mar 02 23:18:43 2012

@author: lims
"""

from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
#import psycopg2 as pg
import sqlite3 as lite
SEXO = ["Masculino","Femenino"]
TIPO_DOC = ["BI","DIRE","PASSAPORTE","CARTA DE CONDUCAO","OUTRO"]
PAISES = [
"�frica do Sul",
"Akrotiri",
"Alb�nia",
"Alemanha",
"Andorra",
"Angola",
"Anguila",
"Ant�rctida ",
"Ant�gua e Barbuda ",
"Antilhas Neerlandesas ",
"Ar�bia Saudita ",
"Arctic Ocean ",
"Arg�lia ",
"Argentina ",
"Arm�nia ",
"Aruba ",
"Ashmore and Cartier Islands ",
"Atlantic Ocean ",
"Austr�lia ",
"�ustria ",
"Azerbaij�o ",
"Baamas ",
"Bangladeche ",
"Barbados ",
"Bar�m ",
"B�lgica ",
"Belize ",
"Benim ",
"Bermudas ",
"Bielorr�ssia ",
"Birm�nia ",
"Bol�via ",
"B�snia e Herzegovina ",
"Botsuana ",
"Brasil ",
"Brunei ",
"Bulg�ria ",
"Burquina Faso ",
"Bur�ndi ",
"But�o ",
"Cabo Verde ",
"Camar�es ",
"Camboja ",
"Canad� ",
"Catar ",
"Cazaquist�o ",
"Chade ",
"Chile ",
"China ",
"Chipre ",
"Clipperton Island ",
"Col�mbia ",
"Comores ",
"Congo-Brazzaville ",
"Congo-Kinshasa ",
"Coral Sea Islands ",
"Coreia do Norte ",
"Coreia do Sul ",
"Costa do Marfim ",
"Costa Rica ",
"Cro�cia ",
"Cuba ",
"Dhekelia ",
"Dinamarca ",
"Dom�nica ",
"Egipto ",
"Emiratos �rabes Unidos ",
"Equador ",
"Eritreia ",
"Eslov�quia ",
"Eslov�nia ",
"Espanha ",
"Estados Unidos ",
"Est�nia ",
"Eti�pia ",
"Faro� ",
"Fiji ",
"Filipinas ",
"Finl�ndia ",
"Fran�a ",
"Gab�o ",
"G�mbia ",
"Gana ",
"Gaza Strip ",
"Ge�rgia ",
"Ge�rgia do Sul e Sandwich do Sul ",
"Gibraltar ",
"Granada ",
"Gr�cia ",
"Gronel�ndia ",
"Guame ",
"Guatemala ",
"Guernsey ",
"Guiana ",
"Guin� ",
"Guin� Equatorial ",
"Guin�-Bissau ",
"Haiti ",
"Honduras ",
"Hong Kong ",
"Hungria ",
"I�men ",
"Ilha Bouvet ",
"Ilha do Natal ",
"Ilha Norfolk ",
"Ilhas Caim�o ",
"Ilhas Cook ",
"Ilhas dos Cocos ",
"Ilhas Falkland ",
"Ilhas Heard e McDonald ",
"Ilhas Marshall ",
"Ilhas Salom�o ",
"Ilhas Turcas e Caicos ",
"Ilhas Virgens Americanas ",
"Ilhas Virgens Brit�nicas ",
"�ndia ",
"Indian Ocean ",
"Indon�sia ",
"Ir�o ",
"Iraque ",
"Irlanda ",
"Isl�ndia ",
"Israel ",
"It�lia ",
"Jamaica",
"Jan Mayen ",
"Jap�o ",
"Jersey ",
"Jibuti ",
"Jord�nia ",
"Kuwait ",
"Laos ",
"Lesoto ",
"Let�nia ",
"L�bano ",
"Lib�ria ",
"L�bia ",
"Listenstaine ",
"Litu�nia ",
"Luxemburgo ",
"Macau ",
"Maced�nia ",
"Madag�scar ",
"Mal�sia ",
"Mal�vi ",
"Maldivas ",
"Mali ",
"Malta ",
"Man, Isle of ",
"Marianas do Norte ",
"Marrocos ",
"Maur�cia ",
"Maurit�nia ",
"Mayotte ",
"M�xico ",
"Micron�sia ",
"Mo�ambique ",
"Mold�via ",
"M�naco ",
"Mong�lia ",
"Monserrate ",
"Montenegro ",
"Mundo ",
"Nam�bia ",
"Nauru ",
"Navassa Island ",
"Nepal ",
"Nicar�gua ",
"N�ger ",
"Nig�ria ",
"Niue ",
"Noruega ",
"Nova Caled�nia ",
"Nova Zel�ndia ",
"Om� ",
"Pacific Ocean ",
"Pa�ses Baixos ",
"Palau ",
"Panam� ",
"Papua-Nova Guin� ",
"Paquist�o ",
"Paracel Islands ",
"Paraguai ",
"Peru ",
"Pitcairn ",
"Polin�sia Francesa ",
"Pol�nia ",
"Porto Rico ",
"Portugal ",
"Qu�nia ",
"Quirguizist�o ",
"Quirib�ti ",
"Reino Unido ",
"Rep�blica Centro-Africana ",
"Rep�blica Checa ",
"Rep�blica Dominicana ",
"Rom�nia ",
"Ruanda ",
"R�ssia ",
"Salvador ",
"Samoa ",
"Samoa Americana ",
"Santa Helena ",
"Santa L�cia ",
"S�o Crist�v�o e Neves ",
"S�o Marinho ",
"S�o Pedro e Miquelon ",
"S�o Tom� e Pr�ncipe ",
"S�o Vicente e Granadinas ",
"Sara Ocidental ",
"Seicheles ",
"Senegal ",
"Serra Leoa ",
"S�rvia ",
"Singapura ",
"S�ria ",
"Som�lia ",
"Southern Ocean ",
"Spratly Islands ",
"Sri Lanca ",
"Suazil�ndia ",
"Sud�o ",
"Su�cia ",
"Su��a ",
"Suriname ",
"Svalbard e Jan Mayen ",
"Tail�ndia ",
"Taiwan ",
"Tajiquist�o ",
"Tanz�nia ",
"Territ�rio Brit�nico do Oceano �ndico ",
"Territ�rios Austrais Franceses ",
"Timor Leste ",
"Togo ",
"Tokelau ",
"Tonga ",
"Trindade e Tobago ",
"Tun�sia ",
"Turquemenist�o ",
"Turquia ",
"Tuvalu ",
"Ucr�nia ",
"Uganda ",
"Uni�o Europeia ",
"Uruguai ",
"Usbequist�o ",
"Vanuatu ",
"Vaticano ",
"Venezuela ",
"Vietname ",
"Wake Island",
"Wallis e Futuna",
"West Bank",
"Z�mbia",
"Zimbabu�"]


class Cliente(QDialog):
    
    def __init__(self,parent=None):
        super(Cliente,self).__init__(parent)
       
        self.accoes()
        self.ui()
        self.db= parent.db

    def ui(self):
        html = """<center style= "{color:blue;}" > <h2 > Cadastro de Clientes </h2> </center> """
        validator = QRegExp(r"\d{1,1}")
        
        titulo = QLabel(html)
        cod = QLabel("Codigo")
        nome = QLabel("Primeiros nomes")
        apelido = QLabel("Apelido")
        endereco = QLabel("Endere�o")
        sexo = QLabel("Sexo")
        email = QLabel("Email")
        nascimento = QLabel("Data de nascimento")
        contacto = QLabel("Contactos")
        emergencia = QLabel("Contactos de Emerg�ncia")
        tipo = QLabel("Tipo de Identifica��o")
        numero = QLabel("N�mero do documento")
        nacionalidade = QLabel("Pa�s")
        validade  = QLabel("Validade do documento")
        obs = QLabel("Observa��es")
        
        calendario = QCalendarWidget()
        calendario1 = QCalendarWidget()
        
        self.cod = QLineEdit()
        self.cod.setMaximumWidth(140)
        self.cod.setObjectName("cod")
        self.cod.setAlignment(Qt.AlignRight)
        self.cod.setEnabled(False)
        self.nome =  QLineEdit()
        self.apelido = QLineEdit()
        self.endereco = QLineEdit()
        self.sexo = QComboBox()
        self.sexo.setMaximumWidth(140)
        self.sexo.addItems(SEXO)
        self.email = QLineEdit()
        self.nascimento = QDateTimeEdit()
        #self.nascimento.setMinimumDate(QDate('1900','01','01'))
        self.nascimento.setDate(QDate.currentDate())
        self.nascimento.setObjectName("cal1")
        self.nascimento.setCalendarPopup(True)
        self.nascimento.setCalendarWidget(calendario)
        self.nascimento.setMaximumWidth(140)
        self.nascimento.setAlignment(Qt.AlignRight)
        self.contacto =  QLineEdit()
        self.emergencia = QLineEdit()
        self.tipo =  QComboBox()
        self.tipo.setMaximumWidth(140)
        self.tipo.addItems(TIPO_DOC)
        self.numero =QLineEdit()
        self.numero.setMaximumWidth(140)
        self.numero.setMaxLength(15)
        self.numero.setAlignment(Qt.AlignRight)
        self.nacionalidade =QComboBox()
        self.nacionalidade.setMaximumWidth(280)
        lista = QStringListModel()
        lista.setStringList(PAISES)
        self.nacionalidade.setModel(lista)

        #self.nacionalidade.addItem(QIcon("./images/ok.png"),"Alo")
        #self.nacionalidade.addItems(self.paises())
        self.validade  = QDateEdit()
        self.validade.setDate(QDate.currentDate())
        #self.validade.setMinimumDate(QDate('1900','01','01'))
        self.validade.setCalendarPopup(True)
        self.validade.setCalendarWidget(calendario1)
        self.validade.setObjectName("cal2")
        self.validade.setMaximumWidth(140)
        self.validade.setAlignment(Qt.AlignRight)
        self.obs =QTextEdit()

        grid = QFormLayout()
        
        grid.addRow(cod           ,self.cod              )
        grid.addRow(nome          ,self.nome             )
        grid.addRow(apelido       ,self.apelido          )
        grid.addRow(endereco      ,self.endereco         )
        grid.addRow(sexo          ,self.sexo             )
        grid.addRow(email         ,self.email            )
        grid.addRow(nascimento    ,self.nascimento       )
        grid.addRow(contacto      ,self.contacto         )
        grid.addRow(emergencia    ,self.emergencia       )
        grid.addRow(tipo          ,self.tipo             )
        grid.addRow(numero        ,self.numero           )
        grid.addRow(nacionalidade ,self.nacionalidade    )
        grid.addRow(validade      ,self.validade         )
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

        self.setWindowTitle("Cadastro de Clientes")
        
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
        self.tool = QToolBar()
        
        gravar = QAction(QIcon("./images/ok.png"),"&Gravar dados",self)
        eliminar = QAction(QIcon("./images/Delete.ico"),"&Eliminar dados",self)
        
        fechar = QAction(QIcon("./images/filequit.png"),"&Fechar",self)
        
        self.tool.addAction(gravar)
        self.tool.addAction(eliminar)
      
        self.tool.addSeparator()
        self.tool.addAction(fechar)

        self.connect(gravar, SIGNAL("triggered()"), self.addRecord)
        self.connect(eliminar, SIGNAL("triggered()"),self.limpar)
        self.connect(fechar, SIGNAL("triggered()"), self.fechar)
        
#==============================================================================   
        
    def fechar(self):
        self.close()
    
    def limpar(self):
        for child in (self.findChildren(QLineEdit) or self.findChildren(QTextEdit)):
            if child.objectName() not in ["cod","cal1","cal2"]: child.clear()

        #gera novo codigo para clientes
        from utilities import codigo
        self.cod.setText("CL" + codigo("OPQRSTUVXYWZ0123456789"))
                
    def connectdb(self):

        self.conn = lite.connect('./db/maindb.db')
        self.cursor = self.conn.cursor()
        self.incrementa()
        self.conn.commit()
    
    def validacao(self):

        if str(self.nome.text()) == "":
            QMessageBox.warning(self,"Erro", "Nome do Cliente inv�lido")
            self.nome.setFocus()
            return False
        else:
            return True

    def accept(self):
        self.mapper.submit()
        QDialog.accept(self)
    
    def mostrarReg(self,cod):
        sql = str("select * from Clientes where cod = %s" %cod)
        self.cursor.execute(sql)
        
        dados = self.cursor.fetchall()
        for item in dados:
            
            self.nome.setText(item[1])
            self.endereco.setText(item[2])
            self.sexo.setCurrentIndex(self.sexo.findText(item[3]))
            self.nacionalidade.setCurrentIndex(self.nacionalidade.findText(item[4]))
            self.tipo.setCurrentIndex(self.tipo.findText(item[5]))
            self.numero.setText(item[6])
            self.nascimento.setDateTime(QDateTime.fromString(item[7]))
            self.validade.setDate(QDate.fromString(item[8]))
            self.emergencia.setText(item[9])
            self.apelido.setText(item[10])
            self.contacto.setText(item[11])
            self.email.setText(item[12])
            self.obs.setPlainText(item[13])

    def addRecord(self):
    
        if self.validacao() == True:
            cod = self.cod.text()
            nome = self.nome.text()
            apelido = self.apelido.text()
            endereco = self.endereco.text()
            sexo = self.sexo.currentText()
            email = self.email.text()
            nascimento = QDateTime(self.nascimento.dateTime()).toString()
            contacto = self.contacto.text()
            emergencia = self.emergencia.text()
            tipo = self.tipo.currentText()
            numero = self.numero.text()
            nacionalidade = self.nacionalidade.currentText()
            validade  = QDate(self.validade.date()).toString()
            obs = self.obs.toPlainText() 
            func1 = "orlando"
            func2 = "orlando"
            estado  ="ocupado"

            if self.parent().actualizar == True:
                sql = """update Clientes set nome = "%s" , endereco = "%s"
                ,sexo = "%s" , nacionalidade = "%s" ,tipo_id ="%s" 
                , numero_id = "%s", nascimento = "%s" ,  validade_id = "%s" ,
                emergencia = "%s", apelido = "%s", contactos = "%s" ,email = "%s"
                , obs ="%s" ,estado = "%s" , func1 = "%s",data = data ,
                func2 = "%s" , data2 = "%s"  where cod = "%s" """ \
                % (nome,endereco,sexo,nacionalidade,tipo,numero,nascimento,
                validade,emergencia,apelido,contacto,email,obs,estado,func1, 
                func2,QDate.currentDate().toString(),self.parent().numeroCliente)
            else:
                values = """"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s", "%s" ,"%s" ,"%s" ,
                "%s","%s" ,"%s"  ,"%s" ,"%s" ,"%s","%s" ,"%s" ,"%s" """ % (cod,
                nome,endereco,sexo,nacionalidade,tipo,numero,nascimento,validade,
                emergencia,apelido,contacto,email,obs,estado,func1,
                QDate.currentDate().toString(),func2,QDate.currentDate().toString())

                print(values)
            try:
                self.db.insert("clientes", values)
                #messagem = QMessageBox.information(self,"Informa��o","Registro Gravado com sucesso!",QMessageBox.Ok)
                
                if QMessageBox.question(self,"Pergunta","Registo Gravado com sucesso!\nDeseja Cadastrar outro Item?",
                               QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
                    self.parent().actualizar = False                
                    self.limpar()
                else:
                    self.close()
                
            except lite.Error as e:
                erro =  "Erro: %s . Reporte ao suporte." % e
                messagem = QMessageBox.critical(self,"Erro","Dados n�o gravados." + erro ,QMessageBox.Ok)
                return

    def closeEvent(self,evt):
        parente =  self.parent()
        parente.encheTabela()
        self.conn.close()
