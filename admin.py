# -*- coding: utf-8 -*-
__author__ = 'Orlando'
import sys

from PyQt4 import QtGui, QtCore, Qt

from Styles import styles
from database import DBCOnnection



style = """
QLabel {
    color: #8a8985;
    font-weight: bold;
    font-size: 11px;
}
"""

style2 = """
QStatusBar {
    background-color: #1283E0;
}
"""

class taskproject(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(taskproject,self).__init__(parent)

        self.db = DBCOnnection('tasks.tsdb')
        #Variaveis usados para controlar Tabs
        self.lista_de_clientes = None
        self.lista_de_tarefas = None
        self.lista_de_usuarios = None
        self.configuracoes = None

        self.clientes = QtGui.QCommandLinkButton("Cadastro de Clientes", "Crie, Edite ou Elimine Clientes.")
        self.connect(self.clientes,QtCore.SIGNAL("clicked()"), self.lista_clientes)
        self.tarefas = QtGui.QCommandLinkButton("Cadastro de Tarefas", "Cadestre e consulte Tarefas a fazer")
        self.connect(self.tarefas,QtCore.SIGNAL("clicked()"),self.lista_tarefas)
        self.users = QtGui.QCommandLinkButton("Cadastro de Usuários", "Crie, Edite ou Elimine usuários.")
        self.config = QtGui.QCommandLinkButton("Cofigurações", "Clica para configurações do sistema.")
        self.sair = QtGui.QCommandLinkButton("&Sair", "Encerra o programa. Termine todas as tarefas antes de fechar o Programa.")
        self.connect(self.sair,QtCore.SIGNAL("clicked()"), self.sair_do_sistema)

        leftpanel = QtGui.QVBoxLayout()
        leftpanel.addWidget(self.clientes)
        leftpanel.addWidget(self.tarefas)
        leftpanel.addWidget(self.users)
        leftpanel.addSpacing(50)
        leftpanel.addWidget(self.config)
        leftpanel.addWidget(self.sair)

        dockPanel = QtGui.QDockWidget("MENU", self)
        table = QtGui.QTableView()

        table.setLayout(leftpanel)
        dockPanel.setWidget(table)

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea,dockPanel)
        self.mainWidget = QtGui.QTabWidget(self)

        tab1 = QtGui.QFrame()
        self.mainWidget.addTab(tab1, "Bem Vindo")

        cetralWidget = QtGui.QWidget(self)
        hLayout = QtGui.QVBoxLayout()

        vLayout = QtGui.QHBoxLayout()
        titulo = QtGui.QLabel("Gestão de Tarefas")
        titulo.setStyleSheet(style)
        minButon = QtGui.QPushButton("")
        minButon.setIcon(QtGui.QIcon("./images/down_arrow_dark.png"))
        minButon.setMaximumWidth(20)
        self.connect(minButon, QtCore.SIGNAL("clicked()"), self.showMinimized)
        closeButon = QtGui.QPushButton()
        closeButon.setIcon(QtGui.QIcon("./images/close_dark.png"))
        self.connect(closeButon, QtCore.SIGNAL("clicked()"), self.sair_do_sistema)
        closeButon.setMaximumWidth(20)
        vLayout.addWidget(titulo)
        vLayout.addWidget(minButon)
        vLayout.addWidget(closeButon)
        menu = QtGui.QTableWidget()
        menu.setMaximumHeight(35)
        menu.setLayout(vLayout)

        hLayout.addWidget(menu)
        hLayout.addWidget(self.mainWidget)

        cetralWidget.setLayout(hLayout)
        self.setCentralWidget(cetralWidget)

        # statusBar = QtGui.QStatusBar()
        # self.setStatusBar(statusBar)
        #Remove windows Borders
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(styles.DARK_BLUE)

    def sair_do_sistema(self):
        sys.exit(True)

    def lista_clientes(self):
        if self.lista_de_clientes == None:
            import listaclientes as tarefas

            janela = tarefas.Listaclientes(self)
            self.lista_de_clientes =  self.mainWidget.addTab(janela,QtGui.QIcon("./images/hotel.png"), "Listagem de Clientes")
            janela.show()
            self.mainWidget.setCurrentIndex(self.lista_de_clientes)
        else:
            for item in range(0,self.mainWidget.count(),1):
                if self.mainWidget.tabText(item) == "Listagem de Clientes":
                    self.mainWidget.setCurrentIndex(item)

    def lista_tarefas(self):
        if self.lista_de_tarefas == None:
            import listaTarefas as tarefas

            janela = tarefas.MainWindow()
            self.lista_de_tarefas =  self.mainWidget.addTab(janela,QtGui.QIcon("./images/hotel.png"), "Lista de Tarefas")
            janela.show()
            self.mainWidget.setCurrentIndex(self.lista_de_tarefas)
        else:
            for item in range(0,self.mainWidget.count(),1):
                if self.mainWidget.tabText(item) == "Lista de Tarefas":
                    self.mainWidget.setCurrentIndex(item)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    textEdit = taskproject()
    textEdit.resize(875,556)
    textEdit.show()
    sys.exit(app.exec_())