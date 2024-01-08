from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
    QMainWindow
    )
# Criando algum widget para ser usado
app = QApplication()

# Criando um Widget base 
base = QWidget()

# Criando Layout 
layout = QVBoxLayout()

# Criando Janela
janela = QMainWindow()


# Mudando a fonte
font = QFont()
font.setPixelSize(90)

# Adicionando o primeiro Widget
label = QLabel('Deixa o like')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)


# Adicionando botão
botao = QPushButton('Botao')
b1 = QPushButton('B1')
b2 = QPushButton('B2')
botao.setFont(font)
layout.addWidget(botao)
layout.addWidget(b1)
layout.addWidget(b2)

# Adicionando o Layout 
base.setLayout(layout)

# Adicionando Janela na Aplicação
janela.setCentralWidget(base)

# Criando menu
menu = janela.menuBar()
arquivo_menu = menu.addMenu('Arquivo')
action = QAction('Print')
arquivo_menu.addAction(action)
# Mostrando a aplicação
janela.show()
app.exec()